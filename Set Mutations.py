"""H = set("Hacker")
R = set("Rank")

#H.update(R)
#print(type(H))
#print(H)

#H.intersection_update(R)
#print(type(H))
#print(H)

H.symmetric_difference_update(R)
print(H)"""

l = int(input())
s = set(map(int, input().split()))

T = int(input())

for i in range(T):
    (x, y) = input().split()
    s2 = set(map(int, input().split()))

    if x == 'intersection_update':
        s.intersection_update(s2)
    elif x == 'update':
        s.update(s2)
    elif x == 'symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif x == 'difference_update':
        s.difference_update(s2)
print(sum(s))
