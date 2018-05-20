"""
ID: sukru2
LANG: PYTHON2
TASK: money
"""

fin = open ("money.in", 'r')
fout = open ("money.out", 'w')

V, N = map(int, fin.readline().split(" "))
ll = map(int, fin.readline().split(" "))

if len(ll) == 1 and V != 1:
    for _ in xrange(V-1):
        ll.append(int(fin.readline()))


dp = [[0 for _ in xrange(len(ll))] for _ in xrange(N+1)]
for i in xrange(len(ll)):
    dp[0][i] = 1

for i in xrange(1, N+1):
    for j in xrange(len(ll)):

        if i - ll[j] >= 0:
            add = dp[i-ll[j]][j]
        else:
            add = 0

        if j > 0:
            noAdd = dp[i][j-1]
        else:
            noAdd = 0

        dp[i][j] = add + noAdd

fout.write("%d\n" % dp[N][len(ll)-1])