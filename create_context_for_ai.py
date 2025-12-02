import os
import json

# Список файлов для объединения
files_to_process = [
    "README.md",
    "Pack_for_GitHub_and_Media/ARTICLE_VC_VK.md",
    "Manifesto_Ancestral_Estates_2.0.md",
    "USER_GUIDE.md",
    "Neuro_Estate_OS.py",
    # Ноутбук сложнее читать как текст, но мы попробуем вытащить из него суть, если он есть
]

output_file = "AI_KNOWLEDGE_BASE.txt"

def read_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Error reading {filepath}: {e}]"

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("=== PROJECT CONTEXT: NEURO-ESTATE ===\n")
    outfile.write("Description: Open Source Framework for Autonomous Settlements (Ancestral Estates 2.0)\n")
    outfile.write("Stack: Python, DAO, Permaculture, AI\n\n")

    for filename in files_to_process:
        if os.path.exists(filename):
            outfile.write(f"\n{'='*30}\n")
            outfile.write(f"FILE: {filename}\n")
            outfile.write(f"{'='*30}\n")
            content = read_file_content(filename)
            outfile.write(content + "\n")
        else:
            print(f"Warning: {filename} not found.")

    # Обработка ноутбука отдельно (вытаскиваем текст из JSON)
    notebook_file = "Neuro_Estate_Simulation.ipynb"
    if os.path.exists(notebook_file):
        outfile.write(f"\n{'='*30}\n")
        outfile.write(f"FILE: {notebook_file} (Converted to Text)\n")
        outfile.write(f"{'='*30}\n")
        try:
            with open(notebook_file, 'r', encoding='utf-8') as f:
                nb_content = json.load(f)
                for cell in nb_content.get('cells', []):
                    if cell.get('cell_type') == 'markdown':
                        outfile.write("".join(cell.get('source', [])) + "\n\n")
                    elif cell.get('cell_type') == 'code':
                        outfile.write("```python\n")
                        outfile.write("".join(cell.get('source', [])))
                        outfile.write("\n```\n\n")
        except Exception as e:
            outfile.write(f"[Error processing notebook: {e}]\n")

print(f"✅ Successfully created {output_file}")
