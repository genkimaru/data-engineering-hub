import os

def add_front_matter(file_path, file_name, weight):
    front_matter = f"---\ntitle: {file_name}\nweight: {weight}\n---\n"
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if len(lines) == 0 or lines[0].strip() != '---':
        with open(file_path, 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(front_matter + content)
        print(f"Processed: {file_path}")

def process_md_files(directory):
    weight = 1
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]
                add_front_matter(file_path, file_name, weight)
                weight += 1

if __name__ == '__main__':
    current_directory = os.getcwd()
    process_md_files(current_directory)
