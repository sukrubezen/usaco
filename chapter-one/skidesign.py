"""
ID: sukru2
LANG: PYTHON2
TASK: skidesign
"""

from bisect import bisect_right, bisect_left

fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')
N = int(fin.readline().strip())

ll = []
for  _ in xrange(N):
    ll.append(int(fin.readline().strip()))

ll.sort()

cost = None
for i in xrange(min(ll), max(ll)+1):
    ind = bisect_right(ll, i + 17)

    upperCost = 0
    for j in xrange(ind, len(ll)):
        upperCost += (ll[j] - (i + 17))**2

    lowerCost = 0
    if ind == len(ll):
        idx = bisect_right(ll, ll[-1] - 17)
        up = ll[-1] - 17
    else:
        idx = bisect_right(ll, i)
        up = i


    for j in xrange(idx-1, -1, -1):
        lowerCost += (up - ll[j])**2


    if cost is None or cost > lowerCost + upperCost:
        cost = lowerCost + upperCost


fout.write("%d\n" % cost)