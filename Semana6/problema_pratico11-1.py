from urllib.request import urlopen


def get_news(url, search):
    response = urlopen(url)
    text = response.read()
    text = text.decode().lower()
    cont = 0
    for txt in search:
        n = text.count(txt)
        print('{} appears {} times.'.format(txt, n))


get_news('http://www.uol.com.br', ['economia', 'clima', 'educação'])
