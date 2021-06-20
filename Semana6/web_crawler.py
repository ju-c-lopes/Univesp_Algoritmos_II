from collector import Collector
from urllib.request import urlopen


def crawl(url):
    """Crawler web recursiva que chama analyze() em cada página web"""
    # analyze() retorna uma lista de URLs de hyperlinks da página Web
    links = analyze(url)

    # Continua recursivamente a verificação de cada link em links
    for link in links:
        try:  # bloco try porque o link pode não ser um arqruivo HTML válido
            crawl(link)
        except:  # se uma exceção for lançada
            pass  # ignora e prossegue


def analyze(url):
    """
    retorna a lista de links http, em formato absoluto,
    na página Web com URL url"""
    print("Visitando ", url)        # para teste
    # Obtém links na página Web
    content = urlopen(url).read()
    content = content.decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.get_links()    # urls é a lista de links
    # análise do conteúdo da página Web ainda a ser feita
    return urls
