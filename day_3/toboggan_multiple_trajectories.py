def read():
    while True:
        try:
            yield input()
        except:
            return

h = 0
indices, counts = [0] * 5, [0] * 5
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for row in read():
    for i, [x, y] in enumerate(slopes):
        if h % y != 0: continue
        if row[indices[i]] == '#': 
            counts[i] += 1
        indices[i] = (indices[i] + x) % len(row)
    h += 1

from functools import reduce
from operator import mul
print(reduce(mul, counts))
