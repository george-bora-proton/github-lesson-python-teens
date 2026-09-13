import os

def read_files():
    contents = ""

    directory = os.getcwd()

    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            with open(os.path.join(directory, file_name), encoding='utf-8') as file:
                file_content = file.read().strip()
                contents += file_content
                contents += "\n"

    return contents