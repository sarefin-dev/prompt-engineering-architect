# Prompt Test Suite

This directory contains the behavioral test suites for the core skills and agent personas. Prompts are code, and they must be tested for regression.

## Structure
Each core skill in the `.claude/skills/` directory should have an accompanying baseline test and skill test here.

- `*-baseline.md`: The raw output of an LLM *before* the skill is applied (proving the failure mode exists).
- `*-skill.md`: The output of the LLM *after* the skill is injected into the context (proving the strict methodology works).
- `pre-deployment-golden.md`: The golden master file used to verify that the `/audit-prompt` command successfully catches structural and vocabulary violations.

## Running Tests
Tests are validated by running the AI agent against the baseline prompts and comparing the output adherence against the golden files.
