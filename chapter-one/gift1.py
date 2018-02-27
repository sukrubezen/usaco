"""
ID: sukru2
LANG: PYTHON2
TASK: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
np = int(fin.readline().strip())

ll = {}
for itr in xrange(np):
    name = fin.readline().strip()
    ll[name] = [0, itr]

dp = {}
while True:
    try:
        name = fin.readline().strip()
        amount, count = map(int, fin.readline().strip().split())
        dp[name] = [amount, count, []]
        for _ in xrange(count):
            nn = fin.readline().strip()
            dp[name][2].append(nn)
    except:
        break


for name in dp:
    amount, count, names = dp[name]
    if count == 0:
        continue
    ll[name][0] -= amount
    ll[name][0] += amount%count
    for nn in names:
        ll[nn][0] += amount/count


tut = sorted(ll.items(), key=lambda x: x[1][1])
for elem in tut:
    fout.write(elem[0]+' ')
    fout.write(str(elem[1][0]) + '\n')