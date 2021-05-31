t = int(input())

for i in range(t):
    x, a = input(), set(input().split())
    y, b = input(), set(input().split())

    print(a.issubset(b))