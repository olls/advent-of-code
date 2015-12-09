import re


def parta(inp):
    return sum(map(lambda x:(1,3)[len(x)>2],re.findall(r'\\"|\\x\w\w|"|\\\\',inp)))


def partb(inp):
    return inp.count('\\')+inp.count('"')+2*len(inp.split('\n'))