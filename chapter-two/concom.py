"""
ID: sukru2
LANG: PYTHON2
TASK: concom
"""

fin = open ("concom.in", 'r')
fout = open ("concom.out", 'w')

N = int(fin.readline())
d = {}

result = {}
for _ in xrange(N):
    fr, to, perc = map(int, fin.readline().split(" "))

    if fr not in d:
        d[fr] = {}
    d[fr][to] = perc

    if perc > 50:
        if fr not in result:
            result[fr] = []

        result[fr].append(to)

for company in result:
    if company not in result[company]:
        result[company].append(company)

while True:
    check = False
    #print result
    for fr in result:
        tmp = {}
        for to in result[fr]:
            if to not in d:
                continue

            for thr in d[to]:
                if thr not in tmp:
                    tmp[thr] = 0

                tmp[thr] += d[to][thr]

        for thr in tmp:
            if tmp[thr] > 50 and thr not in result[fr]:
                check = True
                result[fr].append(thr)
                d[fr][thr] = tmp[thr]

    if not check:
        break

keep = []
for i in result:
    for j in result[i]:
        keep.append([i, j])

keep.sort(key=lambda x: x[1])
keep.sort(key=lambda x: x[0])

for i, j in keep:
    if i != j:
        fout.write("%d %d\n" % (i, j))
        #print "%d %d" % (i, j)