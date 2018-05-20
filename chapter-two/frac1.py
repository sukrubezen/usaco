"""
ID: sukru2
LANG: PYTHON2
TASK: frac1
"""

def gcd(a, b):
    while b:
        a, b = b, a%b

    return a

fin = open ("frac1.in", 'r')
fout = open ("frac1.out", 'w')

N = int(fin.readline().strip())

ll = set()
for deno in xrange(N, 0, -1):
    for nume in xrange(0, deno+1):
        gg = gcd(deno, nume)
        ll.add((nume/gg, deno/gg))

ll = list(ll)
ll.sort(key=lambda x: x[0]/float(x[1]))

for nume, deno in ll:
    fout.write("%d/%d\n" % (nume, deno))