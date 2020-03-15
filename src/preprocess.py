from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

DK_KEYS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ')

with open('../data/da_DK.txt', 'w') as fo:
    with open('../data/da_DK.dic') as fi:
        for i, line in enumerate(fi.readlines()):
            line = line.strip()
            if '(c) Stavekontrolden.dk' in line:
                continue
            if len(line) == 0:
                continue
            word = line.split('/')[0]
            word = ''.join(c for c in word if c.isalpha()).upper()
            spec_chars = [c for c in word if c not in DK_KEYS]
            if len(spec_chars) > 0:
                continue
            fo.write(f'{word}\n')
            if i < 10:
                print (word)

def get_freqs(filename):
    def get_chars(filename):
        with open(filename) as fi:
            for line in fi.readlines():
                for c in line.upper().strip():
                    yield c

    cnt = Counter(get_chars(filename))
    return cnt

freqs = get_freqs('../data/da_DK.txt')
keys = sorted(freqs.keys())
x = keys
y = [freqs[key] for key in keys]
total = sum(y)
y = [val/total for val in y]
plt.bar(x, y)
plt.savefig('../images/frekvenser.png')
with open('../data/frekvenser.csv', 'w') as fo:
    fo.write(f'BOGSTAV,FREKVENS\n')
    for c,f in zip(x,y):
        fo.write(f'{c},{f}\n')
