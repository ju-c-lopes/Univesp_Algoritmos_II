def revert(s):
    if len(s) == 1:
        return s[:-1]
    else:
        return revert(s[:])


print(revert('maravilha'))
# palavra = 'maravilha'
# palavra.
