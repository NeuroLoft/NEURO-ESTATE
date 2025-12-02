import json
import re
import os

input_path = r"c:\Users\admin\Desktop\Проект РП\Release\Pack_for_GitHub_and_Media\Итоги.ipynb"
output_path = r"c:\Users\admin\Desktop\Проект РП\Release\Pack_for_GitHub_and_Media\Итоги_VK.md"

print(f"Reading from: {input_path}")

full_text = ""

try:
    # Try parsing as standard JSON notebook
    with open(input_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)
    
    print("Detected JSON format.")
    
    for cell in notebook_data.get('cells', []):
        cell_type = cell.get('cell_type', '')
        source = cell.get('source', [])
        
        # source can be a list of strings or a single string
        if isinstance(source, list):
            cell_text = "".join(source)
        else:
            cell_text = str(source)
            
        if cell_type == 'code':
            full_text += f"\n```\n{cell_text}\n```\n"
        else:
            full_text += f"{cell_text}\n"

except json.JSONDecodeError:
    print("JSON decode failed. Falling back to text parsing (XML-like format).")
    # Fallback to the previous logic if it's not JSON
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    content_lines = []
    in_cell = False
    current_lang = ""

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("<VSCode.Cell"):
            in_cell = True
            if 'language="markdown"' in line:
                current_lang = "markdown"
            else:
                current_lang = "code"
                content_lines.append("\n```\n")
            continue
        
        if stripped.startswith("</VSCode.Cell>"):
            in_cell = False
            if current_lang == "code":
                content_lines.append("```\n")
            continue

        if in_cell:
            content_lines.append(line)
    
    full_text = "".join(content_lines)

# Apply replacements for VK
# 1. List bullets: Replace '* ' at start of line with '• '
full_text = re.sub(r'(?m)^(\s*)\*\s', r'\1• ', full_text)

# 2. Bold: Remove '**' (User requested to remove bold markers)
full_text = full_text.replace('**', '')

# 3. Italic/Other: Remove remaining '*' (User requested to remove italic markers)
full_text = full_text.replace('*', '')

# Write to output file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_text)

# Verify output
if os.path.exists(output_path):
    size = os.path.getsize(output_path)
    print(f"Successfully converted to: {output_path}")
    print(f"Output file size: {size} bytes")
else:
    print("Error: Output file was not created.")
