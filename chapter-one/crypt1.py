"""
ID: sukru2
LANG: PYTHON2
TASK: crypt1
"""


fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')
M = int(fin.readline().strip())
ll = map(int, fin.readline().strip().split(" "))

from itertools import product

count = 0
for perm in product(ll, repeat = 5):
    a, b, c, d, e = perm

    part1, part2 = (100*a+10*b+c) * d, (100*a+10*b+c) * e
    if  part1 >= 1000 or len(filter(lambda x: int(x) not in ll, list(str(part1)))) != 0:
        continue

    if part2 >= 1000 or len(filter(lambda x: int(x) not in ll, list(str(part2)))) != 0:
        continue

    total = 10*part1 + part2
    if total >= 10000 or len(filter(lambda x: int(x) not in ll, list(str(total)))) != 0:
        continue

    #print a, b, c, d, e
    count += 1

fout.write("%d\n" % count)


