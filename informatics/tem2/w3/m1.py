a=list(input().split())
a=[int(i) for i in a]
for i in range(len(a)):
    print(a[len(a)-i-1],end=" ")