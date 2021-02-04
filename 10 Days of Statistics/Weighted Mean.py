n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a , b)

divider, divisor = 0, 0

for i in range(n):
    divider += a[i]*b[i]
    divisor += b[i]

print("%0.1f" %(divider/divisor))