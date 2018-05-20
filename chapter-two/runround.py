"""
ID: sukru2
LANG: PYTHON2
TASK: runround
"""

from itertools import permutations

fin = open ("runround.in", 'r')
fout = open ("runround.out", 'w')

N = int(fin.readline().strip())

def calc(n):
    keep = map(int, list(str(n)))
    ll = [0 for _ in xrange(len(keep))]
    for itr in xrange(len(keep)):
        ll[itr] = (keep[itr]+itr)%len(keep)

    now = 0
    s = set()
    s.add(0)
    while True:
        now = ll[now]
        if now in s:
            return len(s) == len(keep) and now == 0
        else:
            s.add(now)

    return False


def solve(n, pp):
    for perm in permutations(range(1, 10), pp):
        now = int(''.join(map(str, perm)))
        if now <= n:
            continue
        else:
            if calc(now):
                return now
            else:
                continue

    return None


ll = len(str(N))
for i in xrange(ll, 10):
    result = solve(N, i)
    if result is not None:
        fout.write("%d\n" % result)
        break

