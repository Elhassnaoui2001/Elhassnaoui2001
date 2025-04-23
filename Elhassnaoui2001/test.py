import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

file_path = os.path.join(os.path.dirname(__file__), 'test.py')
content = read_file(file_path)
print(content)