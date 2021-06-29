

"""
d = deque()
d.append(1)
print d
##deque([1])
d.appendleft(2)
print d
##deque([2, 1])
d.clear()
print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
"""
from collections import deque
d = deque()

for _ in range(int(input())):
    i = input().split()
    command = i[0]
    if len(i) > 1:
        e = i[1]
    if command == "append":
        d.append(e)
    elif command == "pop":
        d.pop()
    elif command == "appendleft":
        d.appendleft(e)
    elif command == "popleft":
        d.popleft()

for x in d:
    print(x, end=" " )