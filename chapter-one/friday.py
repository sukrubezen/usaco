"""
ID: sukru2
LANG: PYTHON2
TASK: friday
"""

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')
N = int(fin.readline().strip())

ds = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
normal = [4, 6, 9, 11]

day = 1
month = 1
year = 1900
breakYear = year+N
keep = 0
d = [0, 0, 0, 0, 0, 0, 0]


while True:
    if month == 2:
        leap = False
        if year%100 == 0 and year%400==0:
            leap = True
        elif year%100 != 0 and year%4 == 0:
            leap = True

        if leap:
            if day == 29:
                day = 1
                month += 1
            else:
                day += 1
        else:
            if day == 28:
                day = 1
                month += 1
            else:
                day += 1

    elif month in normal:
        if day == 30:
            day = 1
            month += 1
        else:
            day += 1

    else:
        if day == 31:
            day = 1
            month += 1
        else:
            day += 1


        if month == 13:
            month = 1
            year += 1

    keep += 1
    if year == breakYear:
        break

    if day == 13:
        d[keep%7] += 1

fout.write(' '.join(map(str, d[-2:] + d[:-2])) + '\n')