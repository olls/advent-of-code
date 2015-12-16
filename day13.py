import itertools


def parta(inp):
    people = {}
    for l in inp.split('\n'):
        sign = [-1, 1]['gain' in l]
        words = l.split()
        person, happiness, subject = words[0], int(next(filter(lambda w: w.isdecimal(), words))) * sign, words[-1][:-1]
        people.setdefault(person, {})
        people[person][subject] = happiness
    return max(sum(people[p1][p2] + people[p2][p1] for  p1, p2 in zip(arrangement, (arrangement[-1],)+arrangement)) for arrangement in itertools.permutations(people))


def partb(inp):
    people = {}
    for l in inp.split('\n'):
        sign = [-1, 1]['gain' in l]
        words = l.split()
        person, happiness, subject = words[0], int(next(filter(lambda w: w.isdecimal(), words))) * sign, words[-1][:-1]
        people.setdefault(person, {})
        people[person][subject] = happiness
        people[person]['me'] = 0
    people['me'] = {person: 0 for person in people}
    return max(sum(people[p1][p2] + people[p2][p1] for  p1, p2 in zip(arrangement, (arrangement[-1],)+arrangement)) for arrangement in itertools.permutations(people))