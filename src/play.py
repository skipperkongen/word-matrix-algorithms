import fileinput
import os

import numpy as np

from lib import get_neighbors
from pygtrie import CharTrie

DIR = os.path.dirname(os.path.abspath(__file__))

def to_xy(i):
    return i // 4, i % 4

def to_i(x, y):
    return x * 4 + y

def get_word(ix, board):
    return ''.join([board[i] for i in ix])

# get words where all letters on board
def get_candidates(board):
    with open(f'{DIR}/../data/da_DK.txt') as fi:
        for word in fi.readlines():
            word = word.strip()
            if len([c for c in word if c not in board]) == 0:
                yield word


def search(board):

    # Data structures
    stack = []
    trie = CharTrie()

    # Add candidates to trie
    for cand in get_candidates(board):
        trie[cand] = True

    # Add board indices to stack
    stack = [[i] for i in range(len(board))]

    # Debug info
    print ('Board:\n', np.array(list(board)).reshape(4,4))
    print('Number of candidates:', len(trie))

    # Begin search
    while len(stack) > 0:
        ix = stack.pop()
        word = get_word(ix, board)
        if word in trie:
            yield word
        # Expand last index
        nbs = [to_i(nx,ny) for nx, ny in get_neighbors(*to_xy(ix[-1]))]
        # don't revisit and only expand potential words
        nbs = filter(
            lambda i: i not in ix and trie.has_subtrie(get_word(ix+[i], board)),
            nbs
        )
        for i in nbs:
            new_path = ix + [i]
            stack.append(new_path)


def main():


    # Read board from stdin or file
    board = ''.join([line.strip() for i, line in enumerate(fileinput.input()) if i < 4])
    assert(len(board) == 16)
    print('Read board:', board)

    words = [word for word in set(search(board)) if len(word) > 1]
    print(words)

if __name__=='__main__':
    main()
