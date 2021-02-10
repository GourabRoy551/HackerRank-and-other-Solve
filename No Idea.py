from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr_set = set(arr)
arr_counter = Counter(arr)

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

intersect_ar_a = list(arr_set & set_a)
intersect_ar_b = list(arr_set & set_b)
result = 0
for element in intersect_ar_a:
    result += arr_counter[element]
for element in intersect_ar_b:
    result -= arr_counter[element]

print(result)