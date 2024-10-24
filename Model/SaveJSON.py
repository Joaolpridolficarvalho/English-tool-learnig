import json
from Controller.Instalation import Installation
import os
import random

class SaveJSON:

    def __init__(self):
        self.installation = Installation()
        self.path = self.installation.get_path()

    def __update_json(self, data, path):
        self.__ensure_json_exists(path)
 #       data_existing = self.__read_json(path)
#        data_existing.update(data)
        self.__write_json(data, path)

    def serialize_json_word(self, word, category, examples, audio_path):
        data = {'word': word, 'category': category, 'examples': examples, 'audio_path': [i for i in audio_path]}
        self.save_json_word(data)

    def save_json_config(self, data):
        path = os.path.join(self.path, 'config.json')
        self.__write_json(data, path)

    def save_json_word(self, data):
        path = os.path.join(self.path, 'words.json')
        self.__update_json(data, path)

    def __write_json(self, data, path):
        self.__ensure_json_exists(path)
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

    def __read_json(self, path):
        self.__ensure_json_exists(path)
        with open(path, 'r') as file:
            return json.load(file)

    def __ensure_json_exists(self, path):
        if not os.path.exists(path):
            with open(path, 'w') as file:
                json.dump({}, file, indent=4)

    def shuffle_json(self):
        data = self.__read_json(os.path.join(self.path, 'words.json'))
        random.shuffle(data)
        return data

    def deserialize_json_word(self):
        return self.__read_json(os.path.join(self.path, 'words.json'))