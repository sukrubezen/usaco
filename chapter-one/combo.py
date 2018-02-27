"""
ID: sukru2
LANG: PYTHON2
TASK: combo
"""


fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')
N = int(fin.readline().strip())
l1 = map(int, fin.readline().strip().split(" "))
l2 = map(int, fin.readline().strip().split(" "))

from itertools import product

ll = []
count = 0
for perm in product(range(1, N+1), repeat = 3):
    a, b, c = perm

    if (abs(a-l1[0]) <= 2 or abs(a-l1[0]) >= N-2) and (abs(b-l1[1]) <= 2 or abs(b-l1[1]) >= N-2) and (abs(c-l1[2]) <= 2 or abs(c-l1[2]) >= N-2):
        count += 1
        ll.append([a, b, c])
        continue

    if (abs(a-l2[0]) <= 2 or abs(a-l2[0]) >= N-2) and (abs(b-l2[1]) <= 2 or abs(b-l2[1]) >= N-2) and (abs(c-l2[2]) <= 2 or abs(c-l2[2]) >= N-2):
        count += 1
        ll.append([a, b, c])
        continue

fout.write("%d\n" % count);