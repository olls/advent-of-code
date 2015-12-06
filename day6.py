from PIL import Image


def parta(inp):
    lights = [[0 for x in range(1000)] for y in range(1000)]

    for instruction in inp.split('\n'):
        command = None

        if instruction.startswith('turn on '):
            command = 0
            instruction = instruction[len('turn on '):]

        elif instruction.startswith('toggle '):
            command = 1
            instruction = instruction[len('toggle '):]

        elif instruction.startswith('turn off '):
            command = 2
            instruction = instruction[len('turn off '):]

        start, _, end = instruction.split()
        start = [int(i) for i in start.split(',')]
        end = [int(i) for i in end.split(',')]

        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                lights[y][x] = (1, not lights[y][x], 0)[command]

    im = Image.new('RGB', (1000, 1000), 'white')
    count = 0
    for y, row in enumerate(lights):
        for x, light in enumerate(row):
            if light:
                count += 1
                im.putpixel((x, y), 1)
    im.save('out6', 'png')
    return count


def partb(inp):
    lights = [[0 for x in range(1000)] for y in range(1000)]

    for instruction in inp.split('\n'):
        command = None

        if instruction.startswith('turn on '):
            command = 0
            instruction = instruction[len('turn on '):]

        elif instruction.startswith('toggle '):
            command = 1
            instruction = instruction[len('toggle '):]

        elif instruction.startswith('turn off '):
            command = 2
            instruction = instruction[len('turn off '):]

        start, _, end = instruction.split()
        start = [int(i) for i in start.split(',')]
        end = [int(i) for i in end.split(',')]

        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                lights[y][x] += (1, 2, -1)[command]
                lights[y][x] = max(0, lights[y][x])

    im = Image.new('RGB', (1000, 1000), 'white')
    total = 0
    for y, row in enumerate(lights):
        for x, light in enumerate(row):
            total += light
            im.putpixel((x, y), light)
    im.save('out6', 'png')
    return total
