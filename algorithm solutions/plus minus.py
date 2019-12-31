n = int(input())

arr = list(map(int, input().rstrip().split()))

a=0
b=0
c=0
for i in arr:
    if i>0:
        a=a+1
    if i==0:
        b=b+1
    if i<0:
        c=c+1
print(a/n)

print(c/n)   

print(b/n)


