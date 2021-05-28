x = input()
x1 = set(input().split(" "))

y = input()
y1 = set(input().split(" "))

r = x1.intersection(y1)
print(len(r))