from collector import Collector
from urllib.request import urlopen
from class_crawler import analyze

visited = set()     # inicializa visited como um conjunto vazio


def crawl2(url):
    """
    Um web crawler recursivo que chama analyze()
    sobre cada página web visitada
    """
    # inclui url para conjunto de páginas visitadas
    global visited  # embora não necessário, avisa ao programador
    visited.add(url)
    # analyze() retorna uma lista de URLs de hyperlink no url da página web
    links = analyze(url)

    # Continua a rastejar recursivamente cada link em links
    for link in links:
        # segue o link somente se não for visitado
        if link not in visited:
            try:
                crawl2(link)
            except:
                pass


def analyze(url):
    """
    retorna a lista de links http, em formato absoluto,
    na página Web com URL url"""
    print("Visitando ", url)        # para teste
    # Obtém links na página Web
    content = urlopen(url)
    content = content.read()
    content = content.decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.get_links()    # urls é a lista de links
    # análise do conteúdo da página Web ainda a ser feita
    return urls
