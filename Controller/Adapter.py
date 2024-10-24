import Model.CambridgeRequest as CambridgeRequest
from Model.SaveJSON import SaveJSON
class Adapter:
    def __init__(self):
        self.cambridge = CambridgeRequest.CambridgeRequest()
        self.save_json = SaveJSON()
    def process_request(self, word):
        self.cambridge.process_request(word)

    def return_list(self):
        data = self.save_json.deserialize_json_word()
        return [data] if isinstance(data, dict) else data

    def shuffle_dict(self):
        return self.save_json.shuffle_json()