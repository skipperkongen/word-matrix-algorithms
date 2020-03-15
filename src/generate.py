import os

import numpy as np

DIR = os.path.dirname(os.path.abspath(__file__))

with open(f'{DIR}/../data/frekvenser.csv') as fi:
    pairs = [line.strip().split(',') for line in fi.readlines()]
    pairs = [(p[0],float(p[1])) for p in pairs]
    chars,freqs = zip(*pairs)

rows = np.random.choice(chars, size=16, p=freqs).reshape(4,4)

def select_word(min_len=6, max_len=11):
    with open(f'{DIR}/../data/da_DK.txt') as fi:
        lines = (line.strip() for line in fi.readlines())
        words = [word for word in lines if len(word) >= min_len and len(word) <= max_len]
        return np.random.choice(words)

def get_neighbors(x, y, maxval=3):
    ns = []
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            nx = max(0, min(maxval, x + dx))
            ny = max(0, min(maxval, y + dy))
            if (nx,ny) != (x,y):
                ns.append((nx, ny))
    return set(ns)

def place_word(n):
    used = set()
    x,y = [np.random.choice(4), np.random.choice(4)]
    for _ in range(n):
        used.add((x,y))
        yield x,y
        ns = get_neighbors(x,y).difference(used)
        assert(len(ns)>0)
        x,y = list(ns)[np.random.choice(len(ns))]

random_word = select_word(min_len=5, max_len=8)
placed = False
while not placed:
    try:
        #print('TRY PLACE')
        idx = list(zip(*place_word(len(random_word))))
        placed = True
    except:
        pass

#print(list(idx))
rows[idx[0], idx[1]] = list(random_word)
for row in rows:
    print(''.join(row))

print('Gemt ord:', random_word)
