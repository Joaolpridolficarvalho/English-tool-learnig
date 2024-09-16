import unittest
from Controller.Player import Player
from Model.SaveJSON import SaveJSON
import os
import json


class MyTestCase(unittest.TestCase):

    def test_play_existing_file(self):
        player = Player()
        player.play(r'D:\Documentos\English\English-tool-learnig\model\audio_files\pronunciation_cat_0.mp3')
        self.assertTrue(True)

    def test_play_non_existing_file(self):
        player = Player()
        with self.assertRaises(Exception):
            player.play(r'D:\Documentos\English\English-tool-learnig\model\audio_files\pronunciation_duck_0.mp3')
        self.assertTrue(True)

    def test_write_word_json(self):
        save_json = SaveJSON()
        data = {'word': 'cat', 'category': 'noun', 'examples': ['This is a cat'],
                'audio_path': ['D:/Documentos/English/English-tool-learnig/model/audio_files/pronunciation_cat_0.mp3']}
        with self.assertRaises(Exception):
            save_json.save_json_word(data)
        self.assertTrue(True)

    def test_write_word_json_non_existing(self):
        save_json = SaveJSON()
        path = 'D:/Documentos/English/English-tool-learnig/model/words.json'
        data = {'word': '', 'category': 'noun', 'examples': ['This is a cat'],
                'audio_path': ['D:/Documentos/English/English-tool-learnig/model/audio']}
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        with self.assertRaises(Exception):
            save_json.save_json_word(data)

    def test_write_word_json_duplicate(self):
        path = 'D:/Documentos/English/English-tool-learnig/model/words.json'
        data = {'word': 'cat', 'category': 'noun', 'examples': ['This is a cat'],
                'audio_path': ['D:/Documentos/English/English-tool-learnig/model/audio']}
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        save_json = SaveJSON()
        # First save should succeed
        save_json.save_json_word(data)

        # Second save should raise an exception due to duplicate entry
        with self.assertRaises(Exception):
            save_json.save_json_word(data)
if __name__ == '__main__':
    unittest.main()
