def paper(l, h, w):
    sides = (l * w, w * h, h * l)
    return sum(side * 2 for side in sides) + min(sides)


def parta(inp):
    total = 0
    for p in inp.split('\n'):
        total += paper(*(int(d) for d in p.split('x')))
    return total


def ribbon(l, h, w):
    sides = (2*l + 2*w, 2*w + 2*h, 2*h + 2*l)
    return min(sides) + l * w * h


def partb(inp):
    total = 0
    for p in inp.split('\n'):
        total += ribbon(*(int(d) for d in p.split('x')))
    return total
