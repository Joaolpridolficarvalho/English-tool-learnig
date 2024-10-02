import json
from Controller.Instalation import Installation
import os
import random

class SaveJSON:
    def __init__(self):
        self.installation = Installation()
        self.path = self.installation.get_path()

    def __update_json(self, data, path):
        data_existing = self.__read_json(path)
        self.compare_data(data)
        if data_existing is None:
            data_existing = []

        data_existing.append(data)
        self.__write_json(data_existing, path)

    def serialize_json(self, word, category, examples, audio_path):
        data = {'word': word, 'category': category, 'examples': examples, 'audio_path': [i for i in audio_path]}
        self.save_json_word(data)

    def compare_data(self, data):
        data_existing = self.__read_json(os.path.join(self.path, 'words.json'))
        if data_existing['word'] == data['word']:
            raise Exception('Word already exists')


    def save_json_word(self, data):
        path = os.path.join(self.path, 'words.json')
        self.__update_json(data, path)

    def __write_json(self, data, path):
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
    
    def __read_json(self, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print('Error: ', e)

    def shuffle_json(self ):
        data = self.__read_json(os.path.join(self.path, 'words.json'))
        return random.shuffle(data)

