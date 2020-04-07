from itertools import *
k ,m = map(int, input().split())
n =[]
for _ in range(k):
    n.append(map(int, input().split()[1:]))
maxx = -1
for i in product(*n):
    maxx = max(sum(map(lambda x: x**2, i))%m, maxx)
print(maxx)

