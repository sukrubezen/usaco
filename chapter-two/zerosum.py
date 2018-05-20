"""
ID: sukru2
LANG: PYTHON2
TASK: zerosum
"""

from itertools import product

fin = open ("zerosum.in", 'r')
fout = open ("zerosum.out", 'w')

N = int(fin.readline())

ll = []
for perm in product(['+', '-', ' '], repeat=N-1):
    s = "1"
    sr = "1"

    for i in xrange(1, N):
        if perm[i-1] != ' ':
            s += perm[i-1]

        sr += perm[i-1]
        sr += str(i+1)
        s += str(i+1)

    result = eval(s)
    if result == 0:
        ll.append(sr)

ll.sort()
for elem in ll:
    fout.write("%s\n" % elem)
    #print elem



