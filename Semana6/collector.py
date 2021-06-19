from urllib.parse import urljoin
from html.parser import HTMLParser


class Collector(HTMLParser):
    """Coleta URLs de hyperlink em uma lista"""
    def __init__(self, url):
        """Inicializa analisador, o URL e uma lista"""
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.text = ''

    def handle_starttag(self, tag, attrs):
        """Coleta URLs de hyperlink em sua forma absoluta"""
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # Constrói URL absoluto
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':      # coleta URLs HTTP
                        self.links.append(absolute)

    def get_links(self):
        """Retorna URLs de hyperlink em seyu formato absoluto"""
        return self.links

    def handle_data(self, data):
        """Coleta e concatena dados de texto"""
        self.text += data

    def get_data(self):
        """Retorna a concatenação de todos os dados de texto"""
        temp = self.text.split()
        word = ''
        for txt in temp:
            word += ' ' + txt
        return word
