"""
ID: sukru2
LANG: PYTHON2
TASK: ttwo
"""

fin = open ("ttwo.in", 'r')
fout = open ("ttwo.out", 'w')

ll = []
for i in xrange(10):
    line = fin.readline().strip()
    ll.append(list(line))

fx, fy = None, None
cx, cy = None, None

for i in xrange(10):
    for j in xrange(10):
        if ll[i][j] == 'F':
            fx, fy = i, j
        elif ll[i][j] == 'C':
            cx, cy = i, j

def forward(x, y, dx, dy):
    if 0 <= x+dx < 10 and 0 <= y+dy < 10:
        if ll[x+dx][y+dy] != '*':
            return x+dx, y+dy

    return False

def rotate(dx, dy):
    if dx == 0 and dy == 1:
        return 1, 0
    elif dx == 0 and dy == -1:
        return -1, 0
    elif dx == 1 and dy == 0:
        return 0, -1
    elif dx == -1 and dy == 0:
        return 0, 1


fdx, fdy = -1, 0
cdx, cdy = -1, 0
count = 0
dp = {}
while True:
    if (cx, cy, cdx, cdy, fx, fy, fdx, fdy) in dp:
        #print 0
        fout.write("%d\n" % 0)
        break

    dp[(cx, cy, cdx, cdy, fx, fy, fdx, fdy)] = True

    if fx == cx and fy == cy:
        fout.write("%d\n" % count)
        #print count
        break

    cowResult = forward(cx, cy, cdx, cdy)
    if cowResult != False:
        cx, cy = cowResult
    else:
        cdx, cdy = rotate(cdx, cdy)

    farmerResult = forward(fx, fy, fdx, fdy)
    if farmerResult != False:
        fx, fy = farmerResult
    else:
        fdx, fdy = rotate(fdx, fdy)

    count += 1
