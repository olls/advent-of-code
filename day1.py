def parta(inp):
    return inp.count('(') - inp.count(')')


def partb(inp):
    floor = 0
    for p, c in enumerate(inp):
        floor += int(c == '(') * 2 - 1
        if floor < 0:
            break
    return p + 1
