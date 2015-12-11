def parta(i):
    i = list(i)
    while 1:
        for j in range(len(i)-1, -1, -1):
            i[j] = chr(ord(i[j]) + 1)
            if i[j] > 'z':
                i[j] = 'a'
            else:
                break
        r = d = p = s = a = 0
        for l in i:
            t = s
            s = p
            p = ord(l)
            if s == p-1 and t == s-1:
                r = 1
            if a == p:
                d += 1
                a = 0
            else:
                a = p
        if not any(l in i for l in 'iol') and r and d > 1:
            break
    global b
    b = ''.join(i)
    return b


def partb(i):
    return parta(b)
