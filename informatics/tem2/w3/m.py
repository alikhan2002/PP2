a=list(input().split())
a=[int(i) for i in a]
a.reverse()
for i in range(len(a)):
    print(a[i], end=" ")