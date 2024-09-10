import os

class KeyValueItem:
    def __init__(self, file_path):
        self.file_path = file_path

    def bump_version(self):
        version = 0
        while os.path.exists(self.file_path + f".{version}"):
            version += 1
        return KeyValueItem(self.file_path + f".{version}")

    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def __str__(self):
        return self.file_path
