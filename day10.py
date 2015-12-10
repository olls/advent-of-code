import itertools


def parta(inp, it=40):
    n = list(inp)
    for i in range(it):
        n = ''.join(str(len(list(g)))+ str(k) for k, g in itertools.groupby(n))
    return len(n)


def partb(inp):
    return parta(inp, 50)
