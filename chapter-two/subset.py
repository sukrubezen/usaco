"""
ID: sukru2
LANG: PYTHON2
TASK: subset
"""

fin = open ("subset.in", 'r')
fout = open ("subset.out", 'w')

N = int(fin.readline().strip())

total = (N * (N + 1)) / 2
if total % 2 == 1:
    fout.write("0\n")
else:
    half = total / 2

    dp = {}
    def solve(som, ind):
        if (som, ind) in dp:
            return dp[(som, ind)]

        if ind < 0:
            return 0

        if som == half:
            return 1


        result = 0
        if som - ind >= half:
            result += solve(som-ind, ind-1)

        result += solve(som, ind-1)

        dp[(som, ind)] = result
        return result

    #print solve(total, N) / 2
    fout.write("%d\n" % (solve(total, N) / 2))

