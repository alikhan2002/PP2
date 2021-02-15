a=list(input().split())
a=[int(i) for i in a]
x=int(input())

for i in range(len(a)):
    if(a[i]==x):
        if(x>=0):
            y=int((i+1)%len(a))
            a=a[y:]+a[:i]
        else:
            a=a[-x-i:]+a[:-x-i] 
            print(a)
            break
for i in range(len(a)):
    print(a[i],end=" ")