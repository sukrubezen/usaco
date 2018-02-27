"""
ID: sukru2
LANG: PYTHON2
TASK: beads
"""

fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
N = int(fin.readline().strip())
s = fin.readline().strip()

mox = None
moxGap = None

for gap in xrange(len(s)):
    left = 1
    lk = s[gap-1]
    for l in xrange(2, len(s)+1):
        if lk == 'w':
            lk = s[gap-l]

        if s[gap-l] == 'w':
            left += 1
            continue

        if lk != 'w' and s[gap-l] != lk:
            break

        left += 1

    right = 1
    rk = s[gap%len(s)]
    for r in xrange(1, len(s)):
        if rk == 'w':
            rk = s[(gap+r)%len(s)]

        if s[(gap+r) % len(s)] == 'w':
            right += 1
            continue

        if rk != 'w' and s[(gap+r)%len(s)] != rk:
            break

        right += 1

    #print gap, left, right
    if mox is None or mox < left+right:
        mox = min(left+right, len(s))
        moxGap = gap

#print mox
#print moxGap
fout.write(str(mox) + '\n')
