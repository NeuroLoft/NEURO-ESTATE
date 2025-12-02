import os
import json

# Определяем абсолютный путь к текущей директории скрипта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Список файлов для объединения (относительные пути)
files_to_process = [
    "README.md",
    "FULL_ARTICLE_RESTORED.md", # Восстановленная полная статья
    "Manifesto_Ancestral_Estates_2.0.md",
    "Neuro_Estate_OS.py",
]

output_filename = "AI_KNOWLEDGE_BASE.txt"
output_path = os.path.join(BASE_DIR, output_filename)

def read_file_content(filepath):
    full_path = os.path.join(BASE_DIR, filepath)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Error reading {filepath}: {e}]"

print(f"Starting to assemble context into: {output_path}")

with open(output_path, 'w', encoding='utf-8') as outfile:
    outfile.write("=== PROJECT CONTEXT: NEURO-ESTATE ===\n")
    outfile.write("Description: Open Source Framework for Autonomous Settlements (Ancestral Estates 2.0)\n")
    outfile.write("Stack: Python, DAO, Permaculture, AI\n\n")

    for filename in files_to_process:
        outfile.write(f"\n{'='*30}\n")
        outfile.write(f"FILE: {filename}\n")
        outfile.write(f"{'='*30}\n")
        content = read_file_content(filename)
        outfile.write(content + "\n")

    # Обработка ноутбука
    notebook_file = "Neuro_Estate_Simulation.ipynb"
    full_nb_path = os.path.join(BASE_DIR, notebook_file)
    
    if os.path.exists(full_nb_path):
        outfile.write(f"\n{'='*30}\n")
        outfile.write(f"FILE: {notebook_file} (Converted to Text)\n")
        outfile.write(f"{'='*30}\n")
        try:
            with open(full_nb_path, 'r', encoding='utf-8') as f:
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
    else:
        outfile.write(f"\n[Warning: Notebook {notebook_file} not found]\n")

print(f"✅ SUCCESS! File created at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
