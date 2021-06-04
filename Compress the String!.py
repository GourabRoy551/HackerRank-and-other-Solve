from itertools import groupby

s = str(input())
t = [list(g) for k, g in groupby(s)]

for i in t:
    t = (len(i), int(i[0]))
    print(str(t), end=" ")