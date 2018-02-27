"""
ID: sukru2
LANG: PYTHON2
TASK: ariprog
"""

#
# Read http://eulerarchive.maa.org/docs/translations/E228en.pdf
# "On numbers which are the sum of two squares" by Lenohard Euler
#

fin = open ('ariprog.in', 'r')
fout = open ('ariprog.out', 'w')
N, M = int(fin.readline().strip()), int(fin.readline().strip())

def solve(N, M):
    biSquares = set()
    for i in xrange(M+1):
        for j in xrange(i, M+1):
            biSquares.add(i**2+j**2)

    arr = sorted(list(biSquares))

    ll = []
    mox = arr[-1]
    for itr in xrange(len(arr)):
        a = arr[itr]
        inc = 1
        if 4 <= N < 6:
            inc = 4
        elif 6 <= N < 14:
            inc = 12
        elif N >= 14:
            inc = 84

        for b in xrange(inc, mox+1, inc):
            if a+b*(N-1) > mox:
                break

            check = False
            for i in xrange(N):
                if a+b*i not in biSquares:
                    check = True
                    break
            if not check:
                ll.append([a, b])

    ll.sort(key=lambda x: x[1])

    return ll


ll = solve(N, M)
if len(ll) == 0:
    fout.write("NONE\n")
else:
    for i in xrange(len(ll)):
        fout.write("%d %d\n" % (ll[i][0], ll[i][1]))