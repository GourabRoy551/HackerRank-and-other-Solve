from itertools import combinations

n = int(input())
a = input().split()
b = int(input())

x = list(combinations(a, b))
y = filter(lambda i: 'a' in i, x)
print("{0:.3}".format(len(list(y))/len(x)))