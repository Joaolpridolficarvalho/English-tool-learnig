import requests
from bs4 import BeautifulSoup
from Model.SaveJSON import SaveJSON
import os
from Controller.Instalation import Installation

class CambridgeRequest():

    def __init__(self):
        self.save_json = SaveJSON()

    def __access_url(self,url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        return response

    def get_content_tag(self, tag, class_name, url, element='text'):
        page = self.__access_url(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        results = list()
        for content_tag in soup.find_all(tag, class_=class_name):
            if element == 'text':
                results.append(content_tag.get_text())
            elif element == 'src':
                source_tag = content_tag.find('source')
                results.append(source_tag.get('src'))
        return results

    def get_category(self, url):
        tag = 'span'
        class_name = 'pos dpos'
        result = self.get_content_tag(tag, class_name, url)
        result = str(result).split(',')
        return result

    def get_examples(self, url):
        tag = 'li'
        class_name = 'eg dexamp hax'
        result = self.get_content_tag(tag, class_name, url)
        result = str(result).replace('\n', ' ')
        return result

    def get_link_pronunciation(self, url):
        tag = 'audio'
        class_name = 'hdn'
        result = self.get_content_tag(tag, class_name, url, 'src')
        return result

    def save_pronunciation(self, url, word):
        response = self.download_pronunciation(url)
        audio_path_list = list()
        Installation().create_audio_files_directory()
        for i, audio_link in enumerate(response):
            audio_path = os.path.join(Installation().get_path_audio_files(), f'pronunciation_{word}_{i}.mp3')
            with open(audio_path, 'wb') as file:
                file.write(response[i].content)
            audio_path_list.append(audio_path)
        return audio_path_list

    def download_pronunciation(self, url):
        link = self.get_link_pronunciation(url)
        response_list = list()
        if link:
            for i, audio_link in enumerate(link):
                link_pronunciation = url + audio_link
                response = requests.get(link_pronunciation, headers={'User-Agent': 'Mozilla/5.0'})
                response_list.append(response)

            return response_list

    def process_request(self, word):
        URL = ('https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}'.format(word))
        category = self.get_category(URL)
        examples = self.get_examples(URL)
        audio_path = self.save_pronunciation(URL, word)
        self.save_json.serialize_json_word(word, category, examples, audio_path)
        self.save_page(URL)


# Test
    def save_page(self, URL):
        page = self.__access_url(URL)
        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(page.text)










