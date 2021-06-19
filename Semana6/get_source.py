from urllib.request import urlopen


def get_source(url):
    """Returns the content of resource specified by
    url as a string"""
    response = urlopen(url)
    html = response.read()
    return html.decode()
