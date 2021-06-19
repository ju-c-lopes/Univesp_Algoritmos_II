from html.parser import HTMLParser


class LinkParser(HTMLParser):
    """Analisador de doc. HTML que mostra valores dos
    atributos href nas tags de início de âncora"""

    def handle_starttag(self, tag, attrs):
        """Mostra valor do atributo href, se houver"""

        if tag == 'a':
            # procura atriburo href e mostra seu valor
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])
