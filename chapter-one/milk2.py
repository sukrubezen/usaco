"""
ID: sukru2
LANG: PYTHON2
TASK: milk2
"""

fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')

q = []

N = int(fin.readline().strip())
for _ in xrange(N):
    s, e = map(int, fin.readline().split())
    q.append([s, +1])
    q.append([e, -1])

q.sort(key=lambda x: x[0])
itr = 0
keep = []
while True:
    if itr == len(q) - 1:
        keep.append(q[-1])
        break

    if q[itr][0] == q[itr+1][0]:
        if q[itr][1] + q[itr+1][1] == 0:
            itr += 2
            continue

    keep.append(q[itr])
    itr += 1

q = keep


start, end = None, None
state = 0
moxA, moxB = None, None
for i in xrange(len(q)):
    if state == 0:
        if q[i][1] == 1:
            start = q[i][0]
            state += 1
            if end is not None:
                if moxB is None or moxB < start-end:
                    moxB = start-end
    elif state == 1:
        if q[i][1] == -1:
            end = q[i][0]
            state -= 1
            if moxA is None or moxA < end-start:
                moxA = end-start
        else:
            state += 1
    else:
        state += q[i][1]


    #print state, start, end, moxA, moxB
#print moxA, moxB
if moxB is None:
    moxB = 0
fout.write(str(moxA) + ' ' + str(moxB) + '\n')