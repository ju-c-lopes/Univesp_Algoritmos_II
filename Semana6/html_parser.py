from www_api_python import get_source
from html.parser import HTMLParser


class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])


html = get_source("http://www.uol.com.br")
parser = MyParser()
parser.feed(html)
