k = int(input())
arr = list(map(int, input().split()))

s = set(arr)


cap_room = ((sum(s) * k) - (sum(arr))) // (k - 1)
print(cap_room)
