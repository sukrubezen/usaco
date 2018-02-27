"""
ID: sukru2
LANG: PYTHON2
TASK: barn1
"""
import sys

fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')
M, S, C = map(int, fin.readline().strip().split(" "))

ll = []
for _ in xrange(C):
    temp = int(fin.readline().strip())
    ll.append(temp)

ll.sort()


dp = {}
def solve(ind, stalls):
    if (ind, stalls) in dp:
        return dp[(ind, stalls)]

    if stalls == 1:
        return ll[-1] - ll[ind] + 1

    if ind == len(ll)-1:
        return 1

    res = None
    for i in xrange(ind+1, len(ll)):
        now = solve(i, stalls-1) + ll[i-1] - ll[ind] + 1
        if res is None or res > now:
            res = now

    dp[(ind, stalls)] = res
    return res

fout.write(str(solve(0, M)) + '\n')