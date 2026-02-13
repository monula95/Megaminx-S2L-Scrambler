import random
import collections

F = ['U', 'F', 'L', 'R', 'BL', 'BR']
M = ['', "'", "2", "2'"]
faces = {"F": 0, "R": 1, "BR": 2, "BL": 3, "L": 4}

def scramble(n=49):
    res = ''
    prev_f = None
    dq = collections.deque()

    for i in range(1, n + 1):
        f = random.choice(F)

        if len(dq) >= 2:
            while (
                (f in faces and faces[dq[-2]] == faces[f]
                 and (faces[dq[-1]] - faces[f]) % 5 in {2, 3})
                or (f == prev_f)
            ):
                f = random.choice(F)

            if f in faces:
                dq.append(f)
                dq.popleft()
            else:
                dq.popleft()
                dq.popleft()
        else:
            while f == prev_f:
                f = random.choice(F)
            if f in faces:
                dq.append(f)

        m = random.choice(M)
        prev_f = f

        a = f + m
        a += " " * (4 - len(a))

        if i % 12 == 0:
            res += " " + a + "\n"
        else:
            res += " " + a

    return res