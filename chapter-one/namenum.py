"""
ID: sukru2
LANG: PYTHON2
TASK: namenum
"""

fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')
N = fin.readline().strip()

d= {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y']
}

dd = {}
with open('dict.txt', 'r') as f:
    for word in f:
        dd[word.strip()] = True

def solve(n, sofar):
    if len(n) == 0:
        if sofar in dd:
            return [sofar]
        else:
            return []

    now = n[0]

    if int(now) < 2:
        return []

    results = []

    for elem in d[int(now)]:
        result = solve(n[1:], sofar+elem)
        results += result

    return results


result = solve(list(N), "")
if len(result) == 0:
    fout.write("NONE\n")
else:
    result.sort()
    for res in result:
        fout.write("%s\n" % res)