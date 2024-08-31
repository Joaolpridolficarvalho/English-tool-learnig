import requests
from bs4 import BeautifulSoup
import os


class CambridgeRequest():

    def __init__(self, word):
        self.word = word
        self.URL = ('https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}'.format(self.word))

    def access_url(self):
        response = requests.get(self.URL, headers={'User-Agent': 'Mozilla/5.0'})
        return response

    def get_content_tag(self, tag, class_name, element='text'):
        page = self.access_url()
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

    def get_exemples(self):
        tag = 'span'
        class_name = 'trans dtrans dtrans-se'
        result = self.get_content_tag(tag, class_name)
        result = str(result).replace('\n', ' ')
        return result

    def get_link_pronunciation(self):
        tag = 'audio'
        class_name = 'hdn'
        result = self.get_content_tag(tag, class_name, 'src')
        return result

    def download_pronunciation(self):
        link = self.get_link_pronunciation()
        BASE_URL = 'http://dictionary.cambridge.org'
        if link:
            # Get the current working directory
            current_path = os.getcwd()
            # Create a directory for saving audio files if it doesn't exist
            audio_dir = os.path.join(current_path, 'audio_files')
            if not os.path.exists(audio_dir):
                os.makedirs(audio_dir)
            for i, audio_link in enumerate(link):
                link_pronunciation = BASE_URL + audio_link
                response = requests.get(link_pronunciation, headers={'User-Agent': 'Mozilla/5.0'})
                audio_path = os.path.join(audio_dir, f'pronunciation_{self.word}_{i}.mp3')
                with open(audio_path, 'wb') as file:
                    file.write(response.content)

# TODO: Separate the responsibilities of the class
if __name__ == '__main__':
    word = 'hello'
    cambridge = CambridgeRequest(word)
    print(cambridge.get_exemples())
    print(cambridge.get_category())
    print(cambridge.get_link_pronunciation())
    cambridge.download_pronunciation()