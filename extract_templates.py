import os
import re
import glob

src_dir = r"d:\Learning\prompt engineering book by me\Sorted"
dest_dir = r"d:\Projects\prompt-engineering-architect\templates"

chapter_map = {
    19: "architecture",
    20: "distributed-systems",
    21: "event-driven",
    22: "database",
    23: "reliability",
    24: "security",
    25: "code-review",
    26: "technology-selection",
    27: "documentation",
    28: "financial",
    29: "evaluation",
    30: "observability",
    31: "organizational",
    33: "mcp",
    34: "protocol-aware",
    35: "quality-testing"
}

# Regex to find: ## Template N - Title \n ... ``` \n PROMPT \n ```
template_pattern = re.compile(r'## Template \d+[^—\-]*?[—\-]\s*(.*?)\n(.*?)```(?:[a-zA-Z]*\n)?([\s\S]*?)```', flags=re.IGNORECASE | re.DOTALL)

count = 0

for file_path in glob.glob(os.path.join(src_dir, "chapter-[0-9][0-9]-*.md")):
    filename = os.path.basename(file_path)
    match = re.match(r"chapter-(\d\d)", filename)
    if not match:
        continue
    
    chapter_num = int(match.group(1))
    if chapter_num not in chapter_map:
        continue
        
    category = chapter_map[chapter_num]
    cat_dir = os.path.join(dest_dir, category)
    os.makedirs(cat_dir, exist_ok=True)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all templates in the chapter
    templates = template_pattern.findall(content)
    
    # Let me also try matching just "## Template " to see if headings exist but block doesn't match
    if not templates:
        print(f"No templates extracted from {filename}")
        
    for title, description_block, prompt_text in templates:
        # Sanitize filename
        safe_title = re.sub(r'[^a-zA-Z0-9]+', '-', title.strip()).strip('-').lower()
        if not safe_title:
            continue
            
        file_name = f"{safe_title}.prompt.md"
        out_path = os.path.join(cat_dir, file_name)
        
        # Write the prompt block to the file
        with open(out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(prompt_text.strip() + "\n")
            
        count += 1
        print(f"Extracted: {category}/{file_name}")

print(f"Total templates extracted: {count}")
