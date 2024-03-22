import os

def create_index_md(folder_path):
    folder_name = os.path.basename(folder_path)
    index_md_path = os.path.join(folder_path, '_index.md')

    if not os.path.exists(index_md_path):
        with open(index_md_path, 'w') as file:
            file.write(f"---\n")
            file.write(f"title: {folder_name}\n")
            file.write(f"weight: 0\n")
            file.write(f"---\n")

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            create_index_md(item_path)

current_dir = os.getcwd()
create_index_md(current_dir)
