"""
ID: sukru2
LANG: PYTHON2
TASK: transform
"""

fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
N = int(fin.readline().strip())
ll, lo = [], []
for i in xrange(N):
    ll.append(list(fin.readline().strip()))
for i in xrange(N):
    lo.append(list(fin.readline().strip()))

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

a90d = rotated(ll)
a180d = rotated((a90d))
a270d = rotated((a180d))
reflect = [elem[::-1] for elem in ll]
a90dr = rotated(reflect)
a180dr = rotated((a90dr))
a270dr = rotated((a180dr))

if a90d == lo:
    fout.write("1\n")
elif a180d == lo:
    fout.write("2\n")
elif a270d == lo:
    fout.write("3\n")
elif reflect == lo:
    fout.write("4\n")
elif a90dr == lo or a180dr == lo or a270dr == lo:
    fout.write("5\n")
elif ll == lo:
    fout.write("6\n")
else:
    fout.write("7\n")