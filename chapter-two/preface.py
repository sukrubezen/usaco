"""
ID: sukru2
LANG: PYTHON2
TASK: preface
"""

fin = open ("preface.in", 'r')
fout = open ("preface.out", 'w')

N = int(fin.readline().strip())

d = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

dd = {}
for key in d:
    dd[d[key]] = key

def toRoman(x):
    if x >= 1000:
        return (x / 1000) * d[1000] + toRoman(x % 1000)
    elif x >= 900:
        return d[100] + d[1000] + toRoman(x - 900)
    elif 500 <= x < 900:
        return d[500] + toRoman(x - 500)
    elif x >= 400:
        return d[100] + d[500] + toRoman(x - 400)
    elif 100 <= x < 400:
        return (x / 100) * d[100] + toRoman(x % 100)
    elif x >= 90:
        return d[10] + d[100] + toRoman(x - 90)
    elif 50 <= x < 90:
        return d[50] + toRoman(x - 50)
    elif x >= 40:
        return d[10] + d[50] + toRoman(x - 40)
    elif 10 <= x < 40:
        return (x / 10) * d[10] + toRoman(x % 10)
    elif x == 9:
        return d[1] + d[10]
    elif 5 <= x < 9:
        return d[5] + toRoman(x - 5)
    elif x == 4:
        return d[1] + d[5]
    elif 1 <= x < 4:
        return (x / 1) * d[1]
    else:
        return ""

counts = {}
for i in xrange(1, N+1):
    result = toRoman(i)
    for chr in result:
        if chr not in counts:
            counts[chr] = 0

        counts[chr] += 1

for key, count in sorted(counts.items(), key=lambda x: dd[x[0]]):
    #print key, count
    fout.write("%s %d\n" % (key, count))
