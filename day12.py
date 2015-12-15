import re
import json


def parta(inp):
    return sum(map(int, re.findall(r'-?[0-9]+', inp)))


def partb(inp):
    a=lambda e:(e if type(e)is int else sum(a(ne)for ne in e)if type(e)is list else sum(a(ne)for ne in e.values())if type(e)is dict and'red'not in e.values()else 0);return a(json.loads(inp))