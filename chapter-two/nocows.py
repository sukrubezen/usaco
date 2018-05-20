"""
ID: sukru2
LANG: PYTHON2
TASK: nocows
"""
import math

fin = open ("nocows.in", 'r')
fout = open ("nocows.out", 'w')

N, K = map(int, fin.readline().strip().split(" "))

MOD = 9901

# number of possible trees up to height j for i nodes
dp = [[0 for _ in xrange(K+1)] for _ in xrange(N+1)]


for i in xrange(1, K+1):
    dp[1][i] = 1

for node in xrange(3, N+1, 2):
    for height in xrange(2, K+1):
        dp[node][height] = dp[node][height-1]
        for left in xrange(1, node-1, 2):
            right = node-left-1

            mult = 2
            if left == right:
                mult = 1
            elif left > right:
                break


            lf = (dp[left][height-1] - dp[left][height-2])
            rf = (dp[right][height-1] - dp[right][height-2])

            dp[node][height] += lf * dp[right][height-1] * mult
            dp[node][height] += rf * dp[left][height-1] * mult
            dp[node][height] -= lf * rf * mult


fout.write("%d\n" % ((dp[N][K] - dp[N][K-1]) % MOD))