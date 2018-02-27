"""
ID: sukru2
LANG: PYTHON2
TASK: dualpal
"""

fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')
N, S = map(int, fin.readline().strip().split(" "))

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

count = 0
for i in xrange(S+1, 1000000):
    if count == N:
        break

    check = False
    for base in xrange(2, 11):
        if isP(postProcess(numberToBase(i, base))):
            if check:
                fout.write("%d\n" % i)
                count += 1
                break
            else:
                check = True


