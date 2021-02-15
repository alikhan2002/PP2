a=list(input().split())
a=[int(i) for i in a]
j=0
for i in range(1,len(a)):
    if(a[i]>a[j]):
        print(a[i])
    j+=1