contatos = {
    ('Anna', 'Karenina'): '(123)45-78-90',
    ('Yu', 'Tsun'): '(901)234-56-78',
    ('Hans', 'Castorp'): '(321)908-76-54'
}

agendas = [
    agenda1 := set([value for key, value in contatos.items()]),
    agenda2 := {'(442)321-45-67', '(566)432-10-01'},
    agenda3 := {'(442)321-45-67', '(211)110-11-22'},
    agenda4 := {'(999)849-00-21', '(123)45-78-90'}
]


def sync(ags):
    conj = ags[0]
    for i in range(1, len(ags)):
        conj = conj | ags[i]
    return conj
