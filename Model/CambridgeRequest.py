import requests
from bs4 import BeautifulSoup
import SaveJSON
import os
from Controller.Instalation import Installation

class CambridgeRequest():

    def __init__(self, word):
        self.word = word
        self.URL = ('https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}'.format(self.word))
        self.save_json = SaveJSON.SaveJSON()

    def __access_url(self):
        response = requests.get(self.URL, headers={'User-Agent': 'Mozilla/5.0'})
        return response

    def get_content_tag(self, tag, class_name, element='text'):
        page = self.__access_url()
        soup = BeautifulSoup(page.text, 'html.parser')
        results = list()
        for content_tag in soup.find_all(tag, class_=class_name):
            if element == 'text':
                results.append(content_tag.get_text())
            elif element == 'src':
                source_tag = content_tag.find('source')
                results.append(source_tag.get('src'))
        return results

    def get_category(self):
        tag = 'span'
        class_name = 'pos dpos'
        result = self.get_content_tag(tag, class_name)
        result = str(result).split(',')
        return result

    def get_examples(self):
        tag = 'li'
        class_name = 'eg dexamp hax'
        result = self.get_content_tag(tag, class_name)
        result = str(result).replace('\n', ' ')
        return result

    def get_link_pronunciation(self):
        tag = 'audio'
        class_name = 'hdn'
        result = self.get_content_tag(tag, class_name, 'src')
        return result

    def save_pronunciation(self):
        response = self.download_pronunciation()
        audio_path_list = list()
        Installation().create_audio_files_directory()
        for i, audio_link in enumerate(response):
            audio_path = os.path.join(Installation().get_path_audio_files(), f'pronunciation_{self.word}_{i}.mp3')
            with open(audio_path, 'wb') as file:
                file.write(response[i].content)
            audio_path_list.append(audio_path)
        return audio_path_list

    def download_pronunciation(self):
        link = self.get_link_pronunciation()
        BASE_URL = 'http://dictionary.cambridge.org'
        response_list = list()
        if link:
            for i, audio_link in enumerate(link):
                link_pronunciation = BASE_URL + audio_link
                response = requests.get(link_pronunciation, headers={'User-Agent': 'Mozilla/5.0'})
                response_list.append(response)

            return response_list

    def serialize_json(self):
        word = self.word
        category = self.get_category()
        examples = self.get_examples()
        audio_path = self.save_pronunciation()
        self.save_json.serialize_json(word, category, examples, audio_path)

    def save_page(self, path):
        page = self.access_url()
        with open(path, 'w') as file:
            file.write(page.text)


if __name__ == '__main__':
    word = 'cat'
    cambridge = CambridgeRequest(word)
    print(cambridge.get_examples())
    print(cambridge.get_category())
    print(cambridge.get_link_pronunciation())
    cambridge.save_pronunciation()









