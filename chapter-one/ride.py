"""
ID: sukru2
LANG: PYTHON2
TASK: ride
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
one = fin.readline().strip()
two = fin.readline().strip()

A, B = map(lambda m: reduce(lambda a, b: a*b, map(lambda x: ord(x)-ord('A')+1, list(m))), [one, two])

if A%47 == B%47:
    fout.write('GO\n')
else:
    fout.write('STAY\n')
