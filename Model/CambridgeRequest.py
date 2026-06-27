import aiohttp
import asyncio
from bs4 import BeautifulSoup
from Model.SaveJSON import SaveJSON
import os
from Controller.Instalation import Installation


class CambridgeRequest:
    def __init__(self):
        self.save_json = SaveJSON()

    async def __access_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}) as response:
                return await response.text()
        return response

    async def get_content_tag(self, tag, class_name, url, element="text"):
        page = await self.__access_url(url)
        soup = BeautifulSoup(page, "html.parser")
        results = list()
        for content_tag in soup.find_all(tag, class_=class_name):
            if element == "text":
                results.append(content_tag.get_text())
            elif element == "src":
                source_tag = content_tag.find("source")
                results.append(source_tag.get("src"))
        return results

    async def get_category(self, url):
        tag = "span"
        class_name = "pos dpos"
        result = await self.get_content_tag(tag, class_name, url)
        result = str(result).split(",")
        return result

    async def get_examples(self, url):
        tag = "li"
        class_name = "eg dexamp hax"
        result = await self.get_content_tag(tag, class_name, url)
        result = str(result).replace("\n", " ")
        return result

    async def get_link_pronunciation(self, url):
        tag = "audio"
        class_name = "hdn"
        result = await self.get_content_tag(tag, class_name, url, "src")
        return result

    async def save_pronunciation(self, url, word):
        response = await self.download_pronunciation(url)
        audio_path = list()
        if response:
            installation = Installation()
            path = installation.get_path()
            audio_dir = os.path.join(path, "audio")
            os.makedirs(audio_dir, exist_ok=True)

            for i, audio_data in enumerate(response):
                audio_file_path = os.path.join(audio_dir, f"{word}_{i}.mp3")
                with open(audio_file_path, "wb") as audio_file:
                    audio_file.write(audio_data)
                audio_path.append(audio_file_path)
        return audio_path
    async def download_pronunciation(self, url):
        link = await self.get_link_pronunciation(url)
        response_list = list()
        if link:
            for i, audio_link in enumerate(link):
                link_pronunciation = url + audio_link
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        link_pronunciation, headers={"User-Agent": "Mozilla/5.0"}
                    ) as response:
                        response_list.append(await response.read())

            return response_list

    async def process_request(self, word):
        URL = (
            "https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}".format(
                word
            )
        )
        category = await self.get_category(URL)
        examples = await self.get_examples(URL)
        audio_path = await self.save_pronunciation(URL, word)
        self.save_json.serialize_json_word(word, category, examples, audio_path)
        await self.save_page(URL)

    # Test
    async def save_page(self, URL):
        page = await self.__access_url(URL)
        with open("page.html", "w", encoding="utf-8") as file:
            file.write(page)
