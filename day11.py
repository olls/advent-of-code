import re


def is_invalid(passwd):
    fr = False
    fp = r = p = p2 = 0
    for l in passwd:
        p_ = p
        p = ord(l)
        if p_ == p-1:
            r += 1
        else:
            r = 0
        if r > 1:
            fr = True
        if p2 == p:
            fp += 1
            p2 = 0
        else:
            p2 = p
    if not fr or fp < 2:
        return True
    for l in 'iol':
        if l in passwd:
            return True
    return False


def parta(inp):
    inp = list(inp)
    invalid = True
    while invalid:
        carry = True
        for j in range(len(inp)-1, -1, -1):
            inp[j] = chr(ord(inp[j]) + 1)
            if inp[j] > 'z':
                inp[j] = 'a'
            else:
                break
        invalid = is_invalid(inp)
    global a_ans
    a_ans = ''.join(inp)
    return a_ans


def partb(inp):
    return parta(a_ans)
