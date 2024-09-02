import os

class Installation:
    def __init__(self):
        self.__path = os.curdir
        self.__path_audio_files = os.path.join(self.get_path(), 'audio_files')
    def create_directory(self):
        try:
            os.makedirs(self.get_path())
        except FileExistsError:
            pass

    def create_audio_files_directory(self):
        try:
            os.makedirs(self.get_path_audio_files())
        except FileExistsError:
            pass

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def set_path_audio_files(self):
        self.__path_audio_files = os.path.join(self.get_path(), 'audio_files')

    def get_path_audio_files(self):
        return self.__path_audio_files