# Prompt Engineering Architect

This repository configures Claude Code to operate according to the methodology defined in *Prompt Engineering for Developers & Architects*.

## Custom Commands

### Workflow Commands
*   `/new-prompt` - Create a new APOS-structured prompt template via interactive wizard.
*   `/audit-prompt [file]` - Run the Pre-Deployment Gate (structural and vocabulary audit) on a prompt file.
*   `/refine-prompt [file]` - Iteratively improve a prompt based on specific failure modes.
*   `/extract-variables [file]` - Identify Class 1 (MCP) and Class 2 (Human) variables in a prompt.
*   `/lookup-vocab [term]` - Look up a term from the prompt engineering vocabulary.
*   `/find-template [domain] [concern]` - Search the Part V template library for a matching pattern.

### Specialized Reviewer Personas
Use these commands to activate specific architectural reviewers:
*   `/review-architecture` - Activate the `staff-architect` persona.
*   `/review-database` - Activate the `data-architect` persona.
*   `/review-security` - Activate the `security-architect` persona.
*   `/review-reliability` - Activate the `sre-architect` persona.
*   `/review-code` - Activate the `staff-engineer` persona.

## Default Behavior

When operating in this repository, you should proactively:
1.  **Enforce APOS Structure**: Ensure all generated prompts contain clearly defined Role, Context, Focus, Task, and Output layers.
2.  **Apply Vocabulary Discipline**: Identify and remove weakening terms, preferring Category 1 (Precision) and Category 4 (Constraint) vocabulary.
3.  **Assume Protocol Awareness**: Design prompts assuming MCP availability for live data retrieval where applicable.

## Skill Integration

This configuration loads the following methodological skills automatically:
*   `apos-structure.md`: The canonical 5-layer prompt architecture.
*   `vocabulary-audit.md`: Constraints against probability-reducing language.
*   `reasoning-directives.md`: Application of Category 9 logic flow rules.
*   `output-contract.md`: Formatting schemas and schema validation prompts.
*   `pre-deployment-gate.md`: The mandatory checklist before executing any prompt.
