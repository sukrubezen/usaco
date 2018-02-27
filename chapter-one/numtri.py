"""
ID: sukru2
LANG: PYTHON2
TASK: numtri
"""

fin = open ('numtri.in', 'r')
fout = open ('numtri.out', 'w')
N = int(fin.readline().strip())

ll = []
for _ in xrange(N):
    temp = map(int, fin.readline().split(" "))
    ll.append(temp)


i = N-1
total = N
soms = [0 for _ in xrange(N)]
while True:
    if total == 1:
        break

    temp = []
    for j in xrange(1, total):
        temp.append(max(ll[i][j] + soms[j], ll[i][j-1] + soms[j-1]))

    soms = temp
    total -= 1
    i -= 1


#print soms[0] + ll[0][0]
fout.write("%d\n" % (soms[0] + ll[0][0]))