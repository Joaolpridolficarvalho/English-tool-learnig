import aiohttp
import os
from dataclasses import dataclass

from Model.HandleJSON import HandleJSON
from Controller.Instalation import Installation

class DictionaryRequest:
    def __init__(self):
        self.save_json = HandleJSON()

    async def request(self, word: str):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def download_audio(self, url_audio, word, index):
        installation = Installation()

        audio_dir = os.path.join(
            installation.get_path(),
            "audio"
        )

        os.makedirs(audio_dir, exist_ok=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(url_audio) as response:

                if response.status != 200:
                    return None

                filename = os.path.join(
                    audio_dir,
                    f"{word}_{index}.mp3"
                )

                with open(filename, "wb") as f:
                    f.write(await response.read())

                return filename

    async def process_request(self, word):

        data = await self.request(word)

        if not data:
            return

        categories = []
        examples = []
        audios = []

        phonetics = data[0].get("phonetics", [])

        for i, phonetic in enumerate(phonetics):

            audio = phonetic.get("audio")

            if audio:
                path = await self.download_audio(audio, word, i)

                if path:
                    audios.append(path)

        for meaning in data[0].get("meanings", []):

            categories.append(
                meaning.get("partOfSpeech", "")
            )

            for definition in meaning.get("definitions", []):

                example = definition.get("example")

                if example:
                    examples.append(example)

        self.save_json.serialize_json_word(
            word,
            categories,
            examples,
            audios
        )
