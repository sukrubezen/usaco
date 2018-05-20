"""
ID: sukru2
LANG: PYTHON2
TASK: maze1
"""

fin = open ("maze1.in", 'r')
fout = open ("maze1.out", 'w')

w, h = map(int, fin.readline().split(" "))
d = {}
exits = []

for i in xrange(h):
    lineUp = fin.readline()
    line = fin.readline()

    for j in xrange(w):
        if (i, j) not in d:
            d[(i, j)] = []

        if line[2*j] != '|':
            if j == 0:
                exits.append([i, j])
            else:
                d[(i, j)].append([i, j-1])
                d[(i, j-1)].append([i, j])

        if lineUp[2*j+1] != '-':
            if i == 0:
                exits.append([i, j])
            else:
                d[(i, j)].append([i-1, j])
                d[(i-1, j)].append([i, j])

    if line[2*w] != '|':
        exits.append([i, w-1])

lineUp = fin.readline().strip()

for j in xrange(w):
    if lineUp[2*j+1] != '-':
        exits.append([h-1, j])

tut = [[None for _ in xrange(w)] for _ in xrange(h)]

def solve(x, y, now):
    q = [[x, y, now]]

    while len(q) > 0:
        x, y, now = q.pop(0)

        if tut[x][y] is not None:
            if tut[x][y] <= now:
                continue

        tut[x][y] = now

        for i, j in d[(x, y)]:
            q.append([i, j, now + 1])

#for elem in tut:
#    print '\t'.join(map(str, elem))

for a, b in exits:
    solve(a, b, 1)

#for elem in tut:
#    print '\t'.join(map(str, elem))

mox = 0
for i in xrange(h):
    for j in xrange(w):
        if tut[i][j] is not None:
            if tut[i][j] > mox:
                mox = tut[i][j]

fout.write("%d\n" % mox)
#print mox