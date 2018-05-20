"""
ID: sukru2
LANG: PYTHON2
TASK: sort3
"""

fin = open ("sort3.in", 'r')
fout = open ("sort3.out", 'w')

N = int(fin.readline().strip())
ll = []
for _ in xrange(N):
    ll.append(int(fin.readline().strip()))

counts = [0, 0, 0]
for elem in ll:
    if elem == 1:
        counts[0] += 1
    elif elem == 2:
        counts[1] += 1
    else:
        counts[2] += 1

count = 0
three_coords_twos = []
three_coords_ones = []
for i in xrange(counts[0]+counts[1]):
    if ll[i] == 3:
        if i < counts[0]:
            three_coords_ones.append(i)
        else:
            three_coords_twos.append(i)

for i in xrange(counts[0]+counts[1], N):
    if ll[i] != 3:
        if ll[i] == 2:
            if len(three_coords_twos) != 0:
                ll[i], ll[three_coords_twos[-1]] = ll[three_coords_twos[-1]], ll[i]
                three_coords_twos.pop(-1)
                count += 1
            else:
                ll[i], ll[three_coords_ones[-1]] = ll[three_coords_ones[-1]], ll[i]
                three_coords_ones.pop(-1)
                count += 1
        else:
            if len(three_coords_ones) != 0:
                ll[i], ll[three_coords_ones[-1]] = ll[three_coords_ones[-1]], ll[i]
                three_coords_ones.pop(-1)
                count += 1
            else:
                ll[i], ll[three_coords_twos[-1]] = ll[three_coords_twos[-1]], ll[i]
                three_coords_twos.pop(-1)
                count += 1


two_coords = []
for i in xrange(counts[0]):
    if ll[i] == 2:
        two_coords.append(i)


for i in xrange(counts[0], counts[0]+counts[1]):
    if ll[i] != 2:
        ll[i], ll[two_coords[-1]] = ll[two_coords[-1]], ll[i]
        two_coords.pop(-1)
        count += 1


#print count
fout.write("%d\n" % count)

