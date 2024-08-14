
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}")

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


file_to_write = '07-file-handling\cricket.txt'
content_to_write = 'Hello, this is a sample content for the file.'

    
write_to_file(file_to_write, content_to_write)

content = read_from_file(file_to_write)
print(f"Content read from {file_to_write}:")
print(content)
