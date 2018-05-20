"""
ID: sukru2
LANG: PYTHON2
TASK: cowtour
"""
from heapq import heappush, heappop
from copy import deepcopy

fin = open("cowtour.in", 'r')
fout = open("cowtour.out", 'w')

def dist(a, b):
    a, b = pastures[a], pastures[b]
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


def maxPathDist(fr):
    global dp

    q = []
    heappush(q, [0, fr])
    tut = {}

    while len(q) > 0:
        cost, now = heappop(q)

        if now in tut:
            continue

        dp[fr][now] = cost
        tut[now] = True

        if now not in d:
            continue

        for neighbour in d[now]:
            if neighbour not in tut:
                heappush(q, [cost + dists[now][neighbour], neighbour])

di = {}
def diameter(m):
    if m in di:
        return di[m]

    result = None
    for i in xrange(N):
        if dp[m][i] is None:
            continue

        moxj = None
        for j in xrange(N):
            if dp[j][i] is None:
                continue

            if moxj is None or moxj < dp[j][i]:
                moxj = dp[j][i]

        if result is None or result < moxj:
            result = moxj

    di[m] = result
    return result

df = {}
def farthest(m):
    if m in df:
        return df[m]

    mox = None
    for i in xrange(N):
        if dp[m][i] is None:
            continue

        if mox is None or mox < dp[m][i]:
            mox = dp[m][i]

    df[m] = mox
    return mox

pastures = []
N = int(fin.readline())
for i in xrange(N):
    x, y = map(int, fin.readline().split(" "))
    pastures.append([x, y])

d = {}
for i in xrange(N):
    line = list(fin.readline().strip())
    for j in xrange(N):
        if line[j] == '0':
            continue

        if i not in d:
            d[i] = {}

        if j not in d:
            d[j] = {}

        d[i][j] = dist(i, j)
        d[j][i] = d[i][j]


dists = [[None for _ in xrange(N)] for _ in xrange(N)]
for i in xrange(N):
    for j in xrange(N):
        dists[i][j] = dist(i, j)

dp = [[None for _ in xrange(N)] for _ in xrange(N)]
for i in xrange(N):
    maxPathDist(i)

gMon = None
for i in xrange(N):
    for j in xrange(i+1, N):
        if dp[i][j] is not None:
            continue

        result = max(farthest(i) + farthest(j) + dists[i][j], max(diameter(i), diameter(j)))

        if gMon is None or gMon > result:
            #print i, j, farthest(i), farthest(j), dist(i, j), diameter(i), diameter(j), result
            gMon = result



#print
#for row in dp:
#    print row



#print gMon

fout.write('%f\n' % gMon)
