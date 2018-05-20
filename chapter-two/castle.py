"""
ID: sukru2
LANG: PYTHON2
TASK: castle
"""

fin = open ("castle.in", 'r')
fout = open ("castle.out", 'w')

M, N = map(int, fin.readline().split(" "))

ll = []
for i in xrange(N):
    ll.append(map(int, fin.readline().strip().split(" ")))

d = {}
for i in xrange(N):
    d[i] = {}
    for j in xrange(M):
        d[i][j] = []

for i in xrange(N):
    for j in xrange(M):
        dir = list(bin(ll[i][j])[2:])
        while len(dir) < 4:
            dir.insert(0, "0")

        if dir[0] == "0":
            d[i][j].append([i+1, j])

        if dir[1] == "0":
            d[i][j].append([i, j+1])

        if dir[2] == "0":
            d[i][j].append([i-1, j])

        if dir[3] == "0":
            d[i][j].append([i, j-1])


sofar = {}
def solve(x, y, id):
    sofar[(x, y)] = id

    for a, b in d[x][y]:
        if (a,b) not in sofar:
            solve(a, b, id)

id = 0
for i in xrange(N):
    for j in xrange(M):
        if (i, j) not in sofar:
            id += 1
            solve(i, j, id)

d2 = {}
for key in sofar:
    if sofar[key] not in d2:
        d2[sofar[key]] = []
    d2[sofar[key]].append(key)

ll = [[0 for _ in xrange(M)] for _ in xrange(N)]
for key in d2:
    for a, b in d2[key]:
        ll[a][b] = key

#for row in ll:
#    print row


moxL, point = None, None
for j in xrange(M):
    for i in xrange(N-1, -1, -1):
        if i!= 0 and (ll[i][j] != ll[i-1][j]) and (moxL is None or moxL < len(d2[ll[i][j]]) + len(d2[ll[i-1][j]])):
            moxL = len(d2[ll[i][j]]) + len(d2[ll[i-1][j]])
            point = [i+1, j+1, "N"]

        if j!=M-1 and (ll[i][j] != ll[i][j+1]) and (moxL is None or moxL < len(d2[ll[i][j]]) + len(d2[ll[i][j+1]])):
            moxL = len(d2[ll[i][j]]) + len(d2[ll[i][j+1]])
            point = [i+1, j+1, "E"]



"""print len(d2)
print max(map(lambda x: len(d2[x]), d2))
print moxL
print ' '.join(map(str, point))"""
fout.write("%d\n" % len(d2))
fout.write("%d\n" % max(map(lambda x: len(d2[x]), d2)))
fout.write("%d\n" % moxL)
fout.write("%s\n" % ' '.join(map(str, point)))
