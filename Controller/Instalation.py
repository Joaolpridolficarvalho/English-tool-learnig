import os

class Installation:
    def __init__(self):
        self.__path = os.curdir
        self.__path_audio_files = os.path.join(self.get_path(), 'audio_files')

    def create_directory(self):
        os.makedirs(self.get_path(), exist_ok=True)

    def create_audio_files_directory(self):
        os.makedirs(self.get_path_audio_files(), exist_ok=True)

    def __set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def __set_path_audio_files(self):
        self.__path_audio_files = os.path.join(self.get_path(), 'audio_files')

    def get_path_audio_files(self):
        return self.__path_audio_files