import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        found_marker = False
        for line in lines:
            if found_marker:
                break
            if '%% wiki footer: Please don\'t edit anything below this line %%' in line:
                found_marker = True
            else:
                file.write(line)

def process_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_file(file_path)

process_files_in_directory('.')
