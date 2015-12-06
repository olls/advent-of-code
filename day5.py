import re


def nice_name_a(name):
    if not (sum(name.count(t) for t in 'aeiou') >= 3):
        return False

    double = False
    for p in range(len(name)-1):
        if name[p] == name[p+1]:
            double = True
            break
    if not double:
        return False

    return not any((t in name) for t in ('ab', 'cd', 'pq', 'xy'))


def parta(inp):
    nice_count = 0
    for name in inp.split('\n'):
        nice_count += nice_name_a(name)
    return nice_count


def nice_name_b(name):
    if re.match(r'.*(..).*\1.*', name) is None:
        return False
    if re.match(r'.*(.).\1.*', name) is None:
        return False
    return True


def partb(inp):
    nice_count = 0
    for name in inp.split('\n'):
        nice_count += nice_name_b(name)
    return nice_count
