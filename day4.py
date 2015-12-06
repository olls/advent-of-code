import hashlib


def find_hash(key, n_zeros):
    result = ''
    i = 0
    while not result.startswith('0' * n_zeros):
        result = hashlib.md5(str.encode(key + str(i))).hexdigest()
        i += 1
    return i - 1


def parta(inp):
    return find_hash(inp, 5)

def partb(inp):
    return find_hash(inp, 6)
