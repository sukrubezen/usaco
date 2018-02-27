"""
ID: sukru2
LANG: PYTHON2
TASK: wormhole
"""
from itertools import permutations
from bisect import bisect_right
import sys

sys.setrecursionlimit(10000)

fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
N = int(fin.readline().strip())




def createCombinations(s):
    if len(s) == 2:
        ls = list(s)
        if ls[0][0] > ls[1][0]:
            return [[ls[::-1]]]
        else:
            return [[ls]]

    results = []
    pickedElement = None
    for elem in s:
        pickedElement = elem
        break

    s.remove(pickedElement)

    for elem in s:
        if pickedElement[0] > elem[0]:
            pairNow = [elem, pickedElement]
        else:
            pairNow = [pickedElement, elem]

        temp = createCombinations(s - {elem})
        temp = map(lambda x: x+[pairNow], temp)

        results.extend(temp)

    return results

def nextCoord(pair):
    ind = bisect_right(dy[pair[1]], pair[0])

    if ind == len(dy[pair[1]]):
        return None
    else:
        return (dy[pair[1]][ind], pair[1])

def isLoop(pairs):
    ddc = {}
    for pair in pairs:
        ddc[pair[0]] = pair[1]
        ddc[pair[1]] = pair[0]


    for pair in pairs:
        loopFound = traverse(pair[0], {(pair[1], pair[0])}, ddc, (pair[1], pair[0]))
        if loopFound:
            return True

    for pair in pairs:
        loopFound = traverse(pair[1], {(pair[0], pair[1])}, ddc, (pair[0], pair[1]))
        if loopFound:
            return True


    return False

def traverse(node, sofar, graph, orig):
    nextC = nextCoord(node)
    if nextC is None:
        return False
    else:
        if (node, nextC) == orig:
            return True

        if (node, nextC) in sofar:
            #loop exists but not ours, maybe
            return False

        sofar.add((node, nextC))

        if (nextC, graph[nextC]) == orig:
            return True

        if (nextC, graph[nextC]) in sofar:
            #loop exists but not ours, maybe
            return False

        sofar.add((nextC, graph[nextC]))

        return traverse(graph[nextC], sofar, graph, orig)



ll = list()
dy = {}
for _ in xrange(N):
    x, y = map(int, fin.readline().strip().split(" "))
    ll.append((x, y))
    if y not in dy:
        dy[y] = []
    dy[y].append(x)

combs = createCombinations(set(ll))


for x in dy:
    dy[x].sort()

count = 0
for comb in combs:
    if isLoop(comb):
        count += 1

fout.write("%d\n" % count)

