class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, tb):
        self.file.close()

def count_lines_in_file(filename):
    with FileManager(filename) as file:
        return len(file.readlines())
