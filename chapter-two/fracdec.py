"""
ID: sukru2
LANG: PYTHON2
TASK: fracdec
"""


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

fin = open("fracdec.in", 'r')
fout = open("fracdec.out", 'w')

N, D = map(int, fin.readline().split(" "))


tam = "0"
rest = ""
sofar = {}
if N%D == 0:
    result = str(N/D) + '.0'
else:
    if N > D:
        tam = str(N/D)
        N %= D

    g = gcd(N, D)
    N, D = N/g, D/g

    result = None
    N *= 10
    rest = '.'
    check = True
    while True:
        if N in sofar:
            result = tam + rest[:sofar[N]-1] + '(' + rest[sofar[N]-1:] + ')'
            break

        if N % D == 0:
            rest += str(N/D)
            result = tam + rest
            break
        elif N > D:
            rest += str(N/D)
            sofar[N] = len(rest)
            N %= D
            check = False
        else:
            if check:
                rest += '0'
                sofar[N] = len(rest)
            check = True
            N *= 10

ll = []
for i in xrange(len(result)):
    if i%76 == 0:
        ll.append([])

    ll[-1].append(result[i])

#print '\n'.join(map(lambda row: ''.join(row), ll))
fout.write('\n'.join(map(lambda row: ''.join(row), ll)) + '\n')


