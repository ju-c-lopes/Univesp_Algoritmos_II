from urllib.request import urlopen


def get_source(url):
    response = urlopen(url)
    htm = response.read()
    return htm.decode()


html = get_source("http://www.uol.com.br")
print(html)
