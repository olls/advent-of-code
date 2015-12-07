def parse_value(val, wires):
    val = val.strip()
    if val.isalpha():
        val = wires[val]
    return int(val) & (2**16-1)


def parta(inp):
    wires = {}
    inp = inp.split('\n')
    inp.sort()
    inp.reverse()
    while inp:
        ins = inp.pop()
        func, out = ins.split(' -> ')
        try:
            if 'AND' in func:
                x, y = func.split(' AND ')
                wires[out] = parse_value(x, wires) & parse_value(y, wires)
            elif 'OR' in func:
                x, y = func.split(' OR ')
                wires[out] = parse_value(x, wires) | parse_value(y, wires)
            elif 'LSHIFT' in func:
                x, y = func.split(' LSHIFT ')
                wires[out] = parse_value(x, wires) << parse_value(y, wires)
            elif 'RSHIFT' in func:
                x, y = func.split(' RSHIFT ')
                wires[out] = parse_value(x, wires) >> parse_value(y, wires)
            elif 'NOT' in func:
                _, x = func.split('NOT ')
                wires[out] = ~parse_value(x, wires)
            else:
                wires[out] = parse_value(func, wires)
        except KeyError:
            inp.insert(0, ins)

    return parse_value('a', wires)


def partb(inp):
    a = parta(inp)
    inp = inp.split('\n')
    for i, ins in enumerate(inp):
        if ins.endswith('-> b'):
            inp[i] = str(a) + ' -> b'
            break
    return parta('\n'.join(inp))
