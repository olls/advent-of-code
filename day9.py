import itertools

def parta(inp):
    dists = {}
    for line in inp.split('\n'):
        route, dist = line.split(' = ')
        start, end = route.split(' to ')
        dists.setdefault(start, {})
        dists[start][end] = int(dist)
        dists.setdefault(end, {})
        dists[end][start] = int(dist)

    shortest = 999
    for route in itertools.permutations(dists):
        dist = 0
        prev = route[0]
        for node in route[1:]:
            dist += dists[prev][node]
            prev = node
        if dist < shortest:
            shortest = dist

    return shortest


def partb(inp):
    dists = {}
    for line in inp.split('\n'):
        route, dist = line.split(' = ')
        start, end = route.split(' to ')
        dists.setdefault(start, {})
        dists[start][end] = int(dist)
        dists.setdefault(end, {})
        dists[end][start] = int(dist)

    shortest = 0
    for route in itertools.permutations(dists):
        dist = 0
        prev = route[0]
        for node in route[1:]:
            dist += dists[prev][node]
            prev = node
        if dist > shortest:
            shortest = dist

    return shortest
