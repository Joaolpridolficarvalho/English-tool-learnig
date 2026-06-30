import unittest
from Controller.Player import Player
from Controller.Adapter import Adapter
from Model.SaveJSON import SaveJSON

import os
# This does not test the GUI.
class TestCase(unittest.TestCase):
    def setUp(self):
        self.adapter = Adapter()
        self.adapter.process_request("test")
        self.player = Player()  

    def json_is_valid(self):
        data = self.adapter.return_list()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for item in data:
            self.assertIn("word", item)
            self.assertIn("category", item)
            self.assertIn("examples", item)
            self.assertIn("audio_path", item)

    def player_is_working(self):
        data = SaveJSON().deserialize_json_word()
        file_path = data['audio_path'][0]
        self.player.play(file_path)

    

if __name__ == "__main__":
    TestCase()










            
