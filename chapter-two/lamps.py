"""
ID: sukru2
LANG: PYTHON2
TASK: lamps
"""

from itertools import permutations

fin = open ("lamps.in", 'r')
fout = open ("lamps.out", 'w')

N = int(fin.readline().strip())
C = int(fin.readline().strip())
ons = map(int, fin.readline().strip().split(" "))
offs = map(int, fin.readline().strip().split(" "))

d = {}
for idx in ons:
    if idx < 1:
        continue

    d[idx] = 1

for idx in offs:
    if idx < 1:
        continue

    d[idx] = 0

start = "1" * N
odd = "10" * (N/2)
even = "01" * (N/2)
comp = "100" * (N/3)

if N%2 == 1:
    odd += "1"
    even += "0"
if N%3 == 1:
    comp += "1"
elif N%3 == 2:
    comp += "10"

start = int(start, 2)
odd = int(odd, 2)
even = int(even, 2)
comp = int(comp, 2)


actions = [start, odd, even, comp]

s = set()
s.add(start)
for _ in xrange(C):
    temp = set()
    for cand in s:
        for action in actions:
            temp.add(cand^action)

    s = temp

result = []
for elem in s:
    check = False
    b = bin(elem)[2:]
    b = "0"*(N-len(b)) + b

    for key in d:
        if b[key-1] != str(d[key]):
            #print elem, b, key, d[key]
            check = True
            break
    if not check:
        result.append(elem)

keep = []
for res in result:
    b = bin(res)[2:]
    keep.append("0" * (N-len(b)) + b)

keep.sort()
if len(keep) == 0:
    fout.write("IMPOSSIBLE\n")
else:
    for x in keep:
        fout.write(x + '\n')



