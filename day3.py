def direction(d):
    return {'^': (0, 1),
            'v': (0, -1),
            '>': (1, 0),
            '<': (-1, 0)}[d]


def parta(inp):
    x, y = 0, 0
    visited = {(x, y)}
    for d in inp:
        dx, dy = direction(d)
        x += dx
        y += dy
        visited.add((x, y))

    return len(visited)


def partb(inp):
    s_x, s_y = 0, 0
    r_x, r_y = 0, 0
    visited = {(s_x, s_y)}
    for p in range(len(inp)//2):
        s_d = inp[p*2]
        dx, dy = direction(s_d)
        s_x += dx
        s_y += dy
        visited.add((s_x, s_y))

        r_d = inp[p*2 + 1]
        dx, dy = direction(r_d)
        r_x += dx
        r_y += dy
        visited.add((r_x, r_y))

    return len(visited)
