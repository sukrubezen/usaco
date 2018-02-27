"""
ID: sukru2
LANG: PYTHON2
TASK: palsquare
"""

fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')
N = int(fin.readline().strip())

def isP(x):
    return x == x[::-1]

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def postProcess(ll):
    results = []
    for elem in ll:
        if elem < 10:
            results.append(str(elem))
        else:
            results.append(chr(elem-10+ord('A')))

    return ''.join(results)

for i in xrange(1, 301):
    sq = i**2

    if isP(postProcess(numberToBase(sq, N))):
        fout.write("%s %s\n" % (postProcess(numberToBase(i, N)), postProcess(numberToBase(sq, N))))

