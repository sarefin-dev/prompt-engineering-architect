# Prompt Version Bump Hook

## Trigger Condition
Fires automatically when a file ending in `.prompt.md` is modified within the workspace.

## Description
Enforces configuration management for prompts. Prompts are code; when they change, their versions must change.

## Hook Execution
1.  **Analyze Diff**: Review the modifications made to the `.prompt.md` file.
2.  **Locate Version**: Look for a YAML frontmatter block or a `Version: X.X.X` string in the file.
3.  **Semantic Bump**:
    *   If the structural intent changed (e.g., added a new Output constraint or changed the Role), bump the MINOR version.
    *   If words were swapped or typos fixed (e.g., swapped a Category 2 word for a Category 3 word), bump the PATCH version.
4.  **Auto-Apply**: Update the version string in the file automatically.
5.  **Changelog**: Append a one-line comment at the bottom of the file documenting *why* the prompt was changed (e.g., `Update: tightened negative constraints to prevent hallucination`).
