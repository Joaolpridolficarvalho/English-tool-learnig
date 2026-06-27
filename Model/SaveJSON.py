import json
from Controller.Instalation import Installation
import os
import random


class SaveJSON:
    def __init__(self):
        self.installation = Installation()
        self.path = self.installation.get_path()

    def __read_json(self, file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []
        return data if isinstance(data, list) else [data]

    def __write_json(self, file_path, data):
        # Read existing data if file exists
        existing_data = self.__read_json(file_path) if os.path.exists(file_path) else []

        # Ensure existing data is a list
        if not isinstance(existing_data, list):
            existing_data = [existing_data]

        # Append new data
        if isinstance(data, list):
            existing_data.extend(data)
        else:
            existing_data.append(data)

        # Write complete JSON array
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4)

    def save_json_word(self, data):
        file_path = os.path.join(self.path, "words.json")
        self.__write_json(file_path, data)

    def save_json_config(self, data):
        file_path = os.path.join(self.path, "config.json")
        self.__write_json(file_path, data)

    def serialize_json_word(self, word, category, examples, audio_path):
        data = {
            "word": word,
            "category": category,
            "examples": examples,
            "audio_path": [i for i in audio_path],
        }
        data_list = [data]
        self.save_json_word(data_list)

    def shuffle_json(self):
        data = self.__read_json(os.path.join(self.path, "words.json"))
        random.shuffle(data)
        return data

    def deserialize_json_word(self):
        return self.__read_json(os.path.join(self.path, "words.json"))
