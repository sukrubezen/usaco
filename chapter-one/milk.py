"""
ID: sukru2
LANG: PYTHON2
TASK: milk
"""

fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')
N, M = map(int, fin.readline().strip().split(" "))

ll = []
for i in xrange(M):
    P, A = map(int, fin.readline().strip().split(" "))
    ll.append([P, A])

ll.sort(key = lambda x: x[0])

sofar = 0
cost = 0
for p, a in ll:
    if sofar+a >= N:
        cost += (N-sofar)*p
        break

    sofar += a
    cost += a*p

fout.write(str(cost) + '\n')