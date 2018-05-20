"""
ID: sukru2
LANG: PYTHON2
TASK: hamming
"""

fin = open ("hamming.in", 'r')
fout = open ("hamming.out", 'w')

N, B, D = map(int, fin.readline().strip().split(" "))

def diff(a, b):
    return list(bin(a^b)[2:]).count("1")


d = set()
d.add(0)
d.add(2**D-1)
now = 2**D
while True:
    if len(d) == N:
        break


    check = False
    for elem in d:
        if diff(elem, now) < D:
            check = True
            break

    if not check:
        d.add(now)

    now += 1

#print sorted(list(d))
s = ""
dd = sorted(list(d))
for i in xrange(len(dd)):
    s += str(dd[i]) + " "
    if i % 10 == 9:
        s = s[:-1] + "\n"

if s[-1] != -1:
    s = s[:-1]

fout.write(s+ '\n')