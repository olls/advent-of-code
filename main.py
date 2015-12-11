import sys
import os.path
import importlib


def main():
    day_n = 'day' + sys.argv[1]
    day = importlib.import_module(day_n)

    with open(os.path.join('input', day_n)) as f:
        inp = f.read()

    print(day.parta(inp))
    print(day.partb(inp))


if __name__ == '__main__':
    main()
