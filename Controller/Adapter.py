import Model.CambridgeRequest as CambridgeRequest
import Model.SaveJSON as SaveJSON
class Adapter:
    def __init__(self, word):
        self.cambridge = CambridgeRequest.CambridgeRequest(word)
        self.save_json = SaveJSON.SaveJSON()
    def get_examples(self):
        return self.cambridge.get_examples()

    def get_category(self):
        return self.cambridge.get_category()

    def get_link_pronunciation(self):
        return self.cambridge.get_link_pronunciation()

    def save_pronunciation(self):
        return self.cambridge.save_pronunciation()

    def serialize_json(self):
        self.cambridge.serialize_json()

    def save_page(self, path):
        self.cambridge.save_page(path)

    def get_word(self):
        return self.cambridge.word

    def get_audio_path(self):
        return self.cambridge.save_pronunciation()
