import aiohttp
from bs4 import BeautifulSoup
from Model.SaveJSON import SaveJSON
import os
from Controller.Instalation import Installation
from dataclasses import dataclass

@dataclass
class Element:
    tag: str
    class_name: str
    element: str = "text"

class CambridgeRequest:
    def __init__(self):
        self.save_json = SaveJSON()

    async def __access_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}) as response:
                return await response.text()
        return response

    def content_tag(self, element: Element, page):
        soup = BeautifulSoup(page, "html.parser")
        results = list()
        for content_tag in soup.find_all(element.tag, class_=element.class_name):
            if element.element == "text":
                results.append(content_tag.get_text())
            elif element.element == "src":
                source_tag = content_tag.find("source")
                if source_tag is not None:
                    source = source_tag.get("src")
                    if source:
                        results.append(source)
        return results

    async def save_pronunciation(self, url, word):
        page = await self.__access_url(url)
        audio_element = Element(tag="audio", class_name="hdn", element="src")
        audio_links = self.content_tag(audio_element, page)
        audio_path = list()
        if audio_links:
            installation = Installation()
            path = installation.get_path()
            audio_dir = os.path.join(path, "audio")
            os.makedirs(audio_dir, exist_ok=True)

            for i, audio_link in enumerate(audio_links):
                audio_data = await self.download_pronunciation(audio_link, url)
                audio_file_path = os.path.join(audio_dir, f"{word}_{i}.mp3")
                with open(audio_file_path, "wb") as audio_file:
                    audio_file.write(audio_data)
                audio_path.append(audio_file_path)
        return audio_path

    async def download_pronunciation(self, audio_link, url):
        link_pronunciation = url + audio_link
        async with aiohttp.ClientSession() as session:
            async with session.get(
                link_pronunciation, headers={"User-Agent": "Mozilla/5.0"}
            ) as response:
                return await response.read()

    async def process_request(self, word):
        URL = (
            "https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}".format(
                word
            )
        )
        page = await self.__access_url(URL)
        category_element = Element(tag="span", class_name="pos dpos")
        category = self.content_tag(category_element, page)
        examples_element = Element(tag="li", class_name="eg dexamp hax")
        examples = self.content_tag(examples_element, page)
        audio_path = await self.save_pronunciation(URL, word)
        self.save_json.serialize_json_word(word, category, examples, audio_path)

    
