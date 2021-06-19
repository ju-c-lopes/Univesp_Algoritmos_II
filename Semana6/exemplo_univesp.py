from urllib.request import urlopen, Request
from html.parser import HTMLParser


class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.n_polos = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'item-polos':
                    self.n_polos += 1

    def num_polos(self):
        return self.n_polos


def getSource(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) "
                             "AppleWebkit/537.36 (KHTML, like Gecko) "
                             "Chrome/41.0.2228.0 "
                             "Safari/537.3"}
    reg_url = 'https:XXXXOOOO'
    req = Request(url=url, headers=headers)
    htm = urlopen(req).read()
    return htm.decode()


html = getSource("https://univesp.br/cursos/engenharia-de-computacao")
parser = MyParser()
parser.feed(html)
print(parser.num_polos())
