"""from collections import OrderedDict

x = {}
x['a'] = 1
x['b'] = 2
x['c'] = 3
x['d'] = 4
x['e'] = 5

print(x)

x = OrderedDict()
x['a'] = 1
x['b'] = 2
x['c'] = 3
x['d'] = 4
x['e'] = 5

print(x)"""
from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(" ")
    d[item] = d.get(item, 0) + int(quantity)
for i in d.items():
    print(*i)