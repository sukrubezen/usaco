"""
ID: sukru2
LANG: PYTHON2
TASK: comehome
"""

from heapq import heappush, heappop

fin = open("comehome.in", 'r')
fout = open("comehome.out", 'w')

N = int(fin.readline())
d = {}
for i in xrange(N):
    a, b, dist = fin.readline().split(" ")
    dist = int(dist)

    if a not in d:
        d[a] = {}

    if b not in d:
        d[b] = {}

    if a in d[b]:
        d[b][a] = min(d[b][a], dist)
    else:
        d[b][a] = dist

    if b in d[a]:
        d[a][b] = min(d[a][b], dist)
    else:
        d[a][b] = dist


sofar = {}
q = []
heappush(q, [0, 'Z'])
while len(q) > 0:
    cost, node = heappop(q)

    if node in sofar:
        continue

    sofar[node] = True

    if 'A' <= node <= 'Z' and node != 'Z':
        s =  "%s %d" % (node, cost)
        fout.write(s+'\n')
        break

    if node not in d:
        continue

    for neighbour in d[node]:
        heappush(q, [cost + d[node][neighbour], neighbour])
