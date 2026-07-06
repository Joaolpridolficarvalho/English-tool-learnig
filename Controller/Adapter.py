import Model.CambridgeRequest as CambridgeRequest
from Model.HandleJSON import HandleJSON 
import asyncio


class Adapter:
    def __init__(self):
        self.cambridge = CambridgeRequest.CambridgeRequest()
        self.handle_json = HandleJSON()

    def process_request(self, word):
        asyncio.run(self.cambridge.process_request(word))

    def return_list(self):
        data = self.handle_json.deserialize_json_word()
        return [data] if isinstance(data, dict) else data

    def shuffle_dict(self):
        return self.handle_json.shuffle_json()
