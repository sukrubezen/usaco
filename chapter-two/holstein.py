"""
ID: sukru2
LANG: PYTHON2
TASK: holstein
"""

fin = open ("holstein.in", 'r')
fout = open ("holstein.out", 'w')

V = int(fin.readline().strip())
vv = map(int, fin.readline().strip().split(" "))
G = int(fin.readline().strip())
gg = []
for g in xrange(G):
    gg.append(map(int, filter(lambda x: x!= "", fin.readline().strip().split(" "))))


def diff(a, b):
    count = 0
    for i in xrange(len(a)):
        if a[i] <= b[i]:
            count += b[i] - a[i]
        else:
            return None

    return count

def solve(ll, ind, sofar):
    result = diff(vv, ll)
    #print result, ll, ind, sofar
    if ind == G or result is not None:
        return [result, sofar]

    lll = list(ll)
    for i in xrange(len(ll)):
        lll[i] += gg[ind][i]

    take = solve(lll, ind+1, sofar + [ind])
    notake = solve(ll, ind+1, list(sofar))

    if take[0] is not None and notake[0] is None:
        #print "1", result, ll, ind, sofar, "--", take, notake
        return take
    elif take[0] is None and notake[0] is not None:
        #print 2, result, ll, ind, sofar, "--", take, notake
        return notake
    elif take[0] is None and notake[0] is None:
        #print 3, result, ll, ind, sofar, "--", take, notake
        return [None, []]
    else:
        #print 4, result, ll, ind, sofar, "--", take, notake
        if len(take[1]) < len(notake[1]):
            return take
        else:
            return notake

xx = [0 for i in xrange(V)]
res = solve(xx, 0, [])
#print "%d %s" % (len(res[1]), ' '.join(map(lambda x: str(x+1), res[1])))
fout.write("%d %s\n" % (len(res[1]), ' '.join(map(lambda x: str(x+1), res[1]))))