import unittest
from unittest.mock import patch, MagicMock, AsyncMock
from Controller.Player import Player
from Controller.Adapter import Adapter
from Model.HandleJSON import HandleJSON

import os


# This does not test the GUI.
class TestCase(unittest.TestCase):
    def setUp(self):
        # Mock the network call so tests are deterministic and offline-safe
        with patch("Model.DictionaryRequest.DictionaryRequest.process_request", new_callable=AsyncMock):
            self.adapter = Adapter()
        self.player = Player()

    def test_json_is_valid(self):
        """Return list must be a non-empty list of dicts with the required keys."""
        # Seed a known word entry so the assertion is deterministic
        handle = HandleJSON()
        handle.serialize_json_word("test", ["noun"], ["This is a test."], [])

        data = self.adapter.return_list()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for item in data:
            self.assertIn("word", item)
            self.assertIn("category", item)
            self.assertIn("examples", item)
            self.assertIn("audio_path", item)

    def test_player_is_working(self):
        """Player.play() must return False gracefully when no audio file exists."""
        result = self.player.play("nonexistent_file.mp3")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()










            
