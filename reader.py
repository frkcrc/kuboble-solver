from board import Board

def read(kuboble_str):
    lines = kuboble_str.strip().split('\n')
    moves = int(lines[0])
    if moves <= 0:
        raise ValueError('Invalid goal length')
    lines = lines[1:]
    starts = {}
    targets = {}
    while lines[0][0].isalpha():
        name, si, sj, ti, tj = lines[0].split(',')
        starts[name] = (int(si), int(sj))
        targets[name] = (int(ti), int(tj))
        lines = lines[1:]
    return (moves, Board(lines, starts, targets))