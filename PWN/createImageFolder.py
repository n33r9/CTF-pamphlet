import os
import shutil
import re
import sys

if len(sys.argv) != 2:
    print("Usage: createimg <file_markdown.md>")
    exit(0)

FILE_NAME = sys.argv[1]
FOLDER_IMG = "images"

with open(FILE_NAME, "r", encoding="utf-8") as f:
    data = f.read()

# Tìm các đường dẫn chứa hình ảnh trong nội dung file markdown
image_paths = re.findall(r'!\[.*?\]\((.*?)\)', data)

if not os.path.exists(FOLDER_IMG):
    os.makedirs(FOLDER_IMG)

for path in image_paths:
    if os.path.isabs(path) and os.path.exists(path):
        # Tạo tên file mới cho hình ảnh
        filename = os.path.basename(path)
        # Sao chép hình ảnh vào thư mục images
        dest_path = os.path.join(FOLDER_IMG, filename)
        shutil.copy(path, dest_path)
        # Sửa lại đường dẫn tương đối trong nội dung file markdown
        new_path = os.path.join(FOLDER_IMG, filename).replace("\\", "/")
        data = data.replace(path, new_path)
    else:
        print(f"Warning: Image path '{path}' is not absolute or does not exist.")

# Ghi lại nội dung đã được chỉnh sửa vào file markdown
with open(FILE_NAME, "w", encoding="utf-8") as f:
    f.write(data)

print("Image paths updated and files copied successfully.")
