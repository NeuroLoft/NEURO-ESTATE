import os

search_path = r"c:\Users\admin\Desktop\Проект РП\Release"

print(f"{'File':<50} | {'Size (Bytes)':<15}")
print("-" * 70)

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(".md"):
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)
            print(f"{file:<50} | {size:<15}")
