"""
ID: sukru2
LANG: PYTHON2
TASK: sprime
"""

fin = open ("sprime.in", 'r')
fout = open ("sprime.out", 'w')
N = int(fin.readline().strip())

def isPrime(n, k=10):
    if n == 2 or n == 3:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = ((k*(n-i))%(n-3)) + 2#random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

results = []
q = [2, 3, 5, 7]
while len(q) > 0:
    now = q.pop(0)

    if len(str(now)) == N:
        results.append(now)
        continue

    for i in xrange(10):
        a = 10*now+i
        if isPrime(a):
            q.append(a)


#print '\n'.join(map(str, sorted(results)))
fout.write('\n'.join(map(str, sorted(results))) + '\n')
