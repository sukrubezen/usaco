"""
ID: sukru2
LANG: PYTHON2
TASK: milk3
"""

import sys

sys.setrecursionlimit(10000)

fin = open ('milk3.in', 'r')
fout = open ('milk3.out', 'w')
A, B, C = map(int, fin.readline().split(" "))

dp = {}
now = set()
def solve(a, b, c):
    global now
    #print a, b, c
    if (a, b, c) in dp:
        return
    else:
        dp[(a,b,c)] = True

    if a+b+c != C:
        return

    if a == 0:
        now.add(c)

    if a != 0:
        if B-b >= a:
            solve(0, b+a, c)
        else:
            solve(a-(B-b), B, c)

        if C-c >= a:
            solve(0, b, c+a)
        else:
            solve(a-(C-c), b, C)

    if b != 0:
        if A-a >= b:
            solve(a+b, 0, c)
        else:
            solve(A, b-(A-a), c)

        if C-c >= b:
            solve(a, 0, c+a)
        else:
            solve(a, b-(C-c), C)

    if c != 0:
        if B-b >= c:
            solve(a, b+c, 0)
        else:
            solve(a, B, c-(B-b))

        if A-a >= c:
            solve(a+c, b, 0)
        else:
            solve(A, b, c-(A-a))



solve(0, 0, C)
now = list(now)
now.sort()
#print ' '.join(map(str, now))
fout.write(' '.join(map(str, now)) + '\n')