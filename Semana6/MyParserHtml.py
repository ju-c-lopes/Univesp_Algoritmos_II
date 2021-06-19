from html.parser import HTMLParser


class MyParser(HTMLParser):
    """Analisador de doc. HTML que mostra tags indentadas"""
    def __init__(self):
        """Inicia o analisador e a indentação inicial"""
        HTMLParser.__init__(self)
        self.indent = 0                     # Valor da indentação inicial

    def handle_starttag(self, tag, attrs):
        """
        Mostra tag de inicio com indentação proporcional à
        profundidade do elemento da tag de documento
        """
        if tag not in {'br', 'p'}:
            print('{}{} start'.format(self.indent * ' ', tag))
            self.indent += 4

    def handle_endtag(self, tag):
        """
        Mostra tag de fim com indentação proporcional à
        profundidade do elemento da tag no documento
        """
        if tag not in {'br', 'p'}:
            self.indent -= 4
            print('{}{} end'.format(self.indent * ' ', tag))
