import os

class SaveFile:
    def __init__(self, path):
        self.path = path


    def save(self, file_name, data):
        with open(self.path + file_name, 'a') as f:
            f.write(data)

    def read(self, file_name):
        with open(self.path + file_name, 'r') as f:
            return f.read()
        