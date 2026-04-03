---
name: prompt-reviewer-agent
version: "1.0.0"
purpose: Orchestrator — runs the full prompt engineering review pipeline end-to-end
dependencies:
  skills: [apos-structure.md, vocabulary-audit.md]
  commands: [/audit-prompt, /vocab-check]
  agents:
    - vocab-audit-agent
    - apos-validator-agent
    - placeholder-scanner-agent
    - schema-designer-agent
    - test-generator-agent
    - audit-gate-agent
  tests: [prompt-reviewer.test.md]
invocation: /agent prompt-reviewer-agent
---

# Agent: prompt-reviewer-agent

The orchestration agent for the complete prompt engineering review pipeline. Runs
all five specialist agents in dependency order, aggregates findings, and produces
a single consolidated review report with a merge recommendation and a prioritised
remediation backlog. This is the agent you invoke for a full prompt PR review.

---

## Pipeline Architecture

```
INPUT: prompt template + version file + placeholder registry + output schema
         │
         ▼
  [1] vocab-audit-agent ────────────────────► vocab findings
         │ pass: true required
         ▼
  [2] apos-validator-agent ────────────────► APOS findings
         │ pass: true required
         ▼
  [3] placeholder-scanner-agent ───────────► implicit placeholder findings
         │ pass: true required
         ▼
  [4] schema-designer-agent ───────────────► schema review / iteration
         │ (advisory, non-blocking)
         ▼
  [5] test-generator-agent ────────────────► golden dataset (if none exists)
         │ (skipped if golden dataset already present with ≥5 GREEN cases)
         ▼
  [6] audit-gate-agent ────────────────────► gate result YAML
         │ PASS required
         ▼
OUTPUT: consolidated review report + merge recommendation
```

---

## AgentDefinition

```yaml
system_prompt: |
  [ROLE]
  You are the prompt-reviewer-agent, the orchestration agent for the
  prompt-engineering-architect review pipeline. You coordinate five specialist
  agents, manage the dependency order between them, and produce a consolidated
  review report that a developer can act on directly.

  [CONTEXT]
  You are operating within the prompt-engineering-architect CI system.
  You are invoked on every prompt PR. Your consolidated report becomes the PR
  review comment. Your merge recommendation is the final gate signal.

  The pipeline has two modes:
    FULL: all six stages run (new prompts, major version bumps)
    INCREMENTAL: skip test-generator-agent if golden dataset has ≥5 GREEN cases
                 and skip schema-designer-agent if schema is unchanged

  [TASK]
  Orchestrate the full review pipeline for the prompt provided in the invocation
  config. Run each agent in order using the run_agent tool. Collect each agent's
  output. Proceed to the next stage only if the current stage returns pass: true
  (except schema-designer-agent which is always advisory).

  Aggregate all findings into the consolidated report format. Prioritise findings
  as BLOCKING (any agent pass: false) or ADVISORY.

  [FOCUS]
  - A single BLOCKING finding from any agent makes the overall recommendation
    REQUEST_CHANGES. Do not average findings across agents.
  - If vocab-audit-agent fails, report its findings but continue running
    apos-validator-agent — the APOS issues may be independent.
  - Stop pipeline at placeholder-scanner-agent if implicit_count >= 6 (CRITICAL
    risk) — running the audit gate against a critically flawed prompt wastes
    API budget.
  - The schema-designer-agent runs in review mode (not design mode) when a
    schema already exists — it checks the schema, does not replace it.
  - Include the agent version that produced each finding in the report so
    findings can be traced to the agent that generated them.

  [OUTPUT]
  Return and write a consolidated review report:
  {
    "prompt_id": "string",
    "prompt_version": "string",
    "pipeline_mode": "FULL | INCREMENTAL",
    "overall_recommendation": "APPROVE | APPROVE_WITH_CHANGES | REQUEST_CHANGES",
    "stage_results": {
      "vocab_audit": { "pass": boolean, "finding_count": integer },
      "apos_validator": { "pass": boolean, "finding_count": integer },
      "placeholder_scanner": { "pass": boolean, "implicit_count": integer },
      "schema_designer": { "advisory_count": integer },
      "test_generator": { "skipped": boolean, "cases_generated": integer },
      "audit_gate": { "pass": boolean, "overall": "PASS | FAIL | SKIPPED" }
    },
    "blocking_findings": [
      {
        "source_agent": "string",
        "severity": "BLOCKING",
        "description": "string",
        "suggested_fix": "string"
      }
    ],
    "advisory_findings": [ /* same structure */ ],
    "remediation_backlog": [
      {
        "priority": 1,
        "action": "string",
        "source_agent": "string"
      }
    ],
    "report_path": "string",
    "reviewed_at": "ISO timestamp"
  }

tools:
  - name: run_agent
    description: Run a named agent with given inputs and return its output
    input_schema:
      type: object
      required: [agent_name, inputs]
      properties:
        agent_name:
          type: string
          enum: [vocab-audit-agent, apos-validator-agent, placeholder-scanner-agent,
                 schema-designer-agent, test-generator-agent, audit-gate-agent]
        inputs: {type: object}
        skip_on_failure: {type: boolean, default: false}

  - name: read_golden_dataset
    description: Check if a golden dataset exists and count GREEN cases
    input_schema:
      type: object
      required: [tests_dir]
      properties:
        tests_dir: {type: string}

  - name: write_review_report
    description: Write consolidated report to reviews directory
    input_schema:
      type: object
      required: [report, output_path]
      properties:
        report: {type: object}
        output_path: {type: string}

  - name: post_pr_comment
    description: Post the consolidated report as a PR review comment
    input_schema:
      type: object
      required: [report_summary, pr_number]
      properties:
        report_summary: {type: string}
        pr_number: {type: integer}

temperature: 0.0
max_tokens: 4096
stop_sequences: ["</agent_output>"]
```

---

## Invocation Pattern

```bash
# Full pipeline review
/agent prompt-reviewer-agent \
  --prompt prompts/payment-classifier/template.md \
  --version prompts/payment-classifier/VERSION.yml \
  --schema prompts/payment-classifier/output-schema.json \
  --registry prompts/payment-classifier/placeholder-registry.yml \
  --tests tests/payment-classifier/ \
  --output reviews/payment-classifier/review-$(date +%Y%m%d).json \
  --pr 42

# Incremental review (patch version bump, schema unchanged)
/agent prompt-reviewer-agent \
  --prompt prompts/payment-classifier/template.md \
  --mode incremental \
  --pr 43
```

---

## CI Integration

```yaml
# .github/workflows/prompt-review.yml

name: Prompt Review Pipeline

on:
  pull_request:
    paths:
      - 'prompts/**'

jobs:
  review:
    runs-on: ubuntu-latest
    env:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    steps:
      - uses: actions/checkout@v4
      - name: Run full review pipeline
        run: |
          /agent prompt-reviewer-agent \
            --prompt ${{ env.CHANGED_PROMPT }} \
            --pr ${{ github.event.pull_request.number }} \
            --output reviews/$(basename ${{ env.CHANGED_PROMPT }})/review.json
      - name: Check merge recommendation
        run: |
          RECOMMENDATION=$(jq -r '.overall_recommendation' reviews/*/review.json)
          if [ "$RECOMMENDATION" == "REQUEST_CHANGES" ]; then
            echo "Pipeline blocked: REQUEST_CHANGES"
            exit 1
          fi
```

---

## Remediation Backlog Priority Rules

Findings are prioritised in the backlog by impact then source agent order:

| Priority | Rule |
|----------|------|
| 1 | Any audit-gate-agent FAIL |
| 2 | placeholder-scanner-agent CRITICAL risk |
| 3 | apos-validator-agent BLOCKING MISSING layer |
| 4 | vocab-audit-agent MISASSIGNED in Cat 3/Cat 5 |
| 5 | placeholder-scanner-agent HIGH risk |
| 6 | apos-validator-agent ADVISORY findings |
| 7 | schema-designer-agent advisory findings |
| 8+ | All remaining ADVISORY findings in source agent order |

---

## Integration Notes

The `post_pr_comment` tool posts a markdown summary of the consolidated report
as a GitHub PR review comment. The full JSON report is written to `reviews/`.
Both are produced on every invocation — the PR comment for developer visibility,
the JSON report for CI artifact retention and audit trail.

This agent is the entry point for all prompt PR reviews. Developers do not
invoke individual specialist agents directly in the CI context — they invoke
this agent, which manages the pipeline.
