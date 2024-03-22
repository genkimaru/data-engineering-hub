import os

def process_md_files(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if len(lines) > 0 and lines[0].strip() == '---':
        end_index = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                end_index = i
                break
        
        if end_index != -1:
            with open(file_path, 'w') as file:
                for line in lines[end_index+1:]:
                    file.write(line)
            print(f"Processed: {file_path}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_md_files(file_path)

if __name__ == '__main__':
    current_directory = os.getcwd()
    process_directory(current_directory)
