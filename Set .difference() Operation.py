x = input()
x1 = set(input().split(" "))

y = input()
y1 = set(input().split(" "))

r = x1.difference(y1)
print(len(r))