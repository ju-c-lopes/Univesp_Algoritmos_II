from collector import Collector
from urllib.request import urlopen
from frequency import frequency


class Crawler:
    """Um Web Crawler"""
    def __init__(self):
        """Inicializa visited como um conjunto vazio"""
        self.visited = set()

    def crawl(self, url):
        """Chama analyze() sobre página Web url e chama a si mesma
        sobre cada link para uma página Web não visitada"""

        links = analyze(url)
        self.visited.add(url)
        for link in links:
            if link not in self.visited:
                try:
                    self.crawl(link)
                except:
                    pass


def analyze(url):
    """Exibe a frequência de cada palavra na página Web
    url e exibe e retirna a lista de links http, em formato absoluto"""
    print("Visitando... ", url)     # para teste
    # obtém links na página Web
    content = urlopen(url)
    content = content.read()
    content = content.decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.get_links()    # obtém lista de links

    # calcula frequência de palavras
    cont = collector.get_data()     # obtém dados de texto como string
    freq = frequency(cont)
    # mostra frequência de cada palavra na página Web
    print('\n{:50} {:10} {:5}'.format('URL', 'palavra', 'quant'))
    for word in freq:
        print('{:50} {:10} {:5}'.format(url, word, freq[word]))
    # mostra links http encontrados na página Web
    print('\n{:50} {:10}'. format('URL', 'link'))
    for link in urls:
        print('{:50} {:10}'. format(url, link))
    return urls
