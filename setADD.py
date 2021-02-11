from pip._vendor.distlib.compat import raw_input

num = raw_input()
dist = set()
for i in range(int(num)):
    dist.add(raw_input())
print(len(dist))