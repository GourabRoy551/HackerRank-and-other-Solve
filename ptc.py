# n = int(input())
# a = list(map(int, input().split()))
# print(a)
# #print(type(a))
#
# for i in range(n):
#     if a[i] == a[i+1]:
#         print("OK")
#         break
#     else:
#         print("BYE BYE")

p = input("Write something: ")

print(p)
print(type(p))

x = list(p)
print(x)

for i in range(len(x)):
    if x[i] == x[i+1]:
        print("Go Nuts")
        break