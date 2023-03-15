import sys
from reader import read

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 solver.py <file>')
        exit()
    contents = open(sys.argv[1]).read()
    maxMoves, board = read(contents)