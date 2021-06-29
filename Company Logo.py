from collections import Counter

s = sorted(input())
z = Counter(s).most_common(3)

for x in z:
    print(*x)