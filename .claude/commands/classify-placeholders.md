# /classify-placeholders Command

## Description
Scans an APOS prompt template from the `templates/` library and classifies its `[REQUIRED: ...]` placeholders into Class 1 (MCP), Class 2 (Human Intent), and Class 3 (Structure).

## Invocation
`/classify-placeholders [filename.prompt.md]`

## Execution Flow
1.  Extract all text matching the regex pattern `\[REQUIRED:.*?\]` from the target file.
2.  Apply the `mcp-placeholder-audit.md` skill to categorize each extracted placeholder.
3.  Output a summary table classifying each placeholder:
    *   **Class 1 (Live State)**: Recommend replacing with a specific MCP tool call.
    *   **Class 2 (Intent)**: Leave as manual human input.
    *   **Class 3 (Structure)**: Recommend MCP or manual input based on available infrastructure tools.
4.  Offer to rewrite the prompt to utilize available MCP tools for Class 1 data.
