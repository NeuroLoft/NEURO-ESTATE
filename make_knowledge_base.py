import os

# Пути к файлам
base_path_release = r"c:\Users\admin\Desktop\Проект РП\Release"
base_path_root = r"c:\Users\admin\Desktop\Проект РП"

output_file = os.path.join(base_path_release, "AI_KNOWLEDGE_BASE.txt")

# Список файлов: (Путь к папке, Имя файла)
files_to_process = [
    (base_path_root, "Итоги.md"),  # ГЛАВНАЯ СТАТЬЯ (ЯДРО)
    (base_path_release, "README.md"),
    (base_path_release, "Neuro_Estate_OS.py"),
    (base_path_release, "Manifesto_Ancestral_Estates_2.0.md")
]

print(f"Creating {output_file}...")

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("=== NEURO-ESTATE PROJECT KNOWLEDGE BASE ===\n")
    outfile.write("CORE DOCUMENT: Итоги.md (The Main Article)\n\n")
    
    for base_dir, fname in files_to_process:
        fpath = os.path.join(base_dir, fname)
        if os.path.exists(fpath):
            print(f"Adding {fname}...")
            outfile.write(f"\n\n{'='*40}\nFILE: {fname}\n{'='*40}\n\n")
            try:
                with open(fpath, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
            except Exception as e:
                outfile.write(f"Error reading file: {e}")
        else:
            print(f"WARNING: {fname} not found at {fpath}")

print("DONE")
