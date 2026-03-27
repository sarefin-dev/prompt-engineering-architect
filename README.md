# Prompt Engineering Architect

A workflow operating system that injects rigorous prompt engineering methodology into Claude Code (and other agentic systems). 

This repository operationalizes the standard prompt engineering patterns defined in *Prompt Engineering for Developers & Architects*, including APOS structure, vocabulary discipline, quality gating, and MCP-aware prompt assembly.

Instead of generic behavior, this repository configures Claude Code to act as nine specialized architectural reviewers, using a library of 15 methodological skills and 11 focused slash commands.

## Installation

Choose one of three ways to install the methodology into your Claude Code environment:

```bash
# Option 1 — copy into project (simplest)
cp -r prompt-engineering-architect/.claude ./

# Option 2 — git submodule (keeps updatable)
git submodule add https://github.com/sarefin-dev/prompt-engineering-architect .pe-toolkit
ln -s .pe-toolkit/.claude .claude

# Option 3 — global install (all projects)
cp -r .claude/skills ~/.claude/skills
cp -r .claude/agents ~/.claude/agents
cp -r .claude/commands ~/.claude/commands
```

## How It Works

This system leverages three mechanisms to change baseline agent behavior into methodology-driven behavior:

1.  **Skills (`.claude/skills/`)**: Methodological rules (like APOS structure or failure taxonomies) injected into the context window at execution time.
2.  **Agents (`.claude/agents/`)**: Pre-configured system prompts that combine specific skills for targeted analytical tasks.
3.  **Hooks (`.claude/hooks/`)**: Automated quality gates that intercept prompt execution to verify structural and vocabulary compliance.

## Structural Components

*   **`README.md`**: This overview.
*   **`CLAUDE.md`**: The root configuration file that loads the system.
*   **`.claude/skills/`**: 15 skill files (methodology execution rules).
*   **`.claude/agents/`**: 9 agent personas (specialized reviewers).
*   **`.claude/commands/`**: 11 slash commands (workflow accelerators).
*   **`.claude/hooks/`**: Automated execution and pre-deployment gates.
*   **`vocabulary/`**: YAML-structured definitions of the 9 vocabulary categories.
*   **`templates/`**: The domain-specific prompt template library (200+ APOS templates).
*   **`tests/`**: RED-GREEN test pairs proving the efficacy of the injected methodology.
*   **`examples/`**: End-to-end worked examples of workflow execution.

## Core Capabilities

By installing this system, your agent gains the ability to:

*   Assemble prompts using the canonical **APOS (Role, Context, Focus, Task, Output)** architecture.
*   Enforce the 9 categories of analytical **Vocabulary Discipline**, recognizing weakening and strengthening terms.
*   Execute the **Pre-Deployment Gate**, rejecting prompts that lack structure or contain probability-reducing vocabulary.
*   Apply **Category 9 Reasoning Directives**, such as "verify against retrieved data before concluding."
*   Assemble **Protocol-Aware Prompts**, intelligently routing missing context to MCP retrieval (Class 1) or manual input (Class 2).

## Reference Map

*   **APOS Structure**: See Chapter 5. Operationalized in `.claude/skills/apos-structure.md`.
*   **Vocabulary Discipline**: See Chapters 2 & 3. Operationalized in `.claude/skills/vocabulary-audit.md` and `vocabulary/`.
*   **Output Control**: See Chapter 9. Operationalized in `.claude/skills/output-contract.md`.
*   **Quality Gates**: See Chapter 10. Operationalized in `.claude/skills/pre-deployment-gate.md` and `.claude/hooks/`.
*   **Reasoning Directives**: See Chapter 12 and 34. Operationalized in `.claude/skills/reasoning-directives.md`.
*   **Tree of Thought**: See Chapter 12 (§12.6). Operationalized in `.claude/skills/tot-reasoning.md`.
*   **Agentic Patterns**: See Chapter 16 (ReAct & Plan-and-Execute). Operationalized in `.claude/skills/react-pattern.md` and `.claude/skills/plan-execute.md`.
*   **File-Based Context**: See Chapter 7 (§7.8). Operationalized in `.claude/skills/file-context.md`.
*   **Local Inference Routing**: See Chapter 30. Operationalized in `.claude/skills/local-inference.md`.
*   **MCP Prompt Engineering**: See Chapter 33 & 34. Operationalized in `.claude/skills/mcp-prompting.md`.
