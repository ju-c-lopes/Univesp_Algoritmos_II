contatos = {
    ('Anna', 'Karenina'): '(123)45-78-90',
    ('Yu', 'Tsun'): '(901)234-56-78',
    ('Hans', 'Castorp'): '(321)908-76-54'
}


def lookup(agenda):
    """Consulta uma agenda existente"""
    search_name = input('Digite o nome: ')
    search_lastname = input('Digite o sobrenome: ')
    if (search_name, search_lastname) in agenda:
        return agenda[(search_name, search_lastname)]
