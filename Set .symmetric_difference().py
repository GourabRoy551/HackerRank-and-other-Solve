x = input()
x1 = set(input().split(" "))

y = input()
y1 = set(input().split(" "))

r = x1.symmetric_difference(y1)
print(len(r))