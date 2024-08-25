import requests
from bs4 import BeautifulSoup
import os


class CambridgeRequest():

    def __init__(self, word):
        self.URL = ('https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}'.format(word))

    def access_url(self):
        response = requests.get(self.URL, headers={'User-Agent': 'Mozilla/5.0'})
        return response

    def get_content_tag(self, page, tag, class_name):
        soup = BeautifulSoup(page.text, 'html.parser')
        results = list()
        for content_tag in soup.find_all(tag, class_=class_name):
            results.append(content_tag.text)
        return results

    

if __name__ == '__main__':
    word = 'hello'
    cambridge = CambridgeRequest(word)
    page = cambridge.access_url()
    category = cambridge.get_content_tag(page, 'span', 'pos dpos')
    print('Category:' + str(category))
    exemples = cambridge.get_content_tag(page, 'span', 'trans dtrans dtrans-se')
    print('exemples:' + str(exemples))


