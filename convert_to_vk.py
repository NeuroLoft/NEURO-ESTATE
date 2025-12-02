import re
import os

input_path = r"c:\Users\admin\Desktop\Итоги.ipynb"
output_path = r"c:\Users\admin\Desktop\Итоги_VK.md"

print(f"Reading from: {input_path}")

# Read the file
with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Extract content from XML-like structure
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
            content_lines.append("\n```\n") # Add code block start
        continue
    
    if stripped.startswith("</VSCode.Cell>"):
        in_cell = False
        if current_lang == "code":
            content_lines.append("```\n") # Add code block end
        continue

    if in_cell:
        content_lines.append(line)

full_text = "".join(content_lines)

# Apply replacements
# 1. List bullets: Replace '* ' at start of line with '• '
# We use a regex that matches start of line (^), optional whitespace (\s*), asterisk (\*), and space (\s)
# We capture the whitespace in group 1 to preserve indentation
full_text = re.sub(r'(?m)^(\s*)\*\s', r'\1• ', full_text)

# 2. Bold: Replace '**' with '__'
# This preserves bold formatting in Markdown but removes asterisks
full_text = full_text.replace('**', '__')

# 3. Italic/Other: Replace remaining '*' with '_'
# This preserves italic formatting in Markdown but removes asterisks
full_text = full_text.replace('*', '_')

# Write to output file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Successfully converted to: {output_path}")
