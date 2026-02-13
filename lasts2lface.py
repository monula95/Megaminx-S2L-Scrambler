import random
import collections

F = ['U', 'F', 'R']
M = ['', "'", "2", "2'"]

def Rmove(count, res):
    count, res = add_move("R", count, res)
    m = random.choice(M)
    a = 'U' + m
    count, res = add_move(a, count, res)
    count, res = add_move("R'", count, res)
    return count, res


def add_move(move, count, res):
    count += 1

    move += " " * (4 - len(move))

    if count % 12 == 0:
        res += " " + move + "\n"
    else:
        res += " " + move
    return count, res

def scramble(n=36):
    res = ''
    prev_f = None
    count = 0

    while count < n:
        f = random.choice(F)

        while f == prev_f:
            f = random.choice(F)

        if f == 'R':
            count, res = Rmove(count, res)

        else:
            m = random.choice(M)
            a = f + m
            count, res = add_move(a, count, res)

        prev_f = f

    return res