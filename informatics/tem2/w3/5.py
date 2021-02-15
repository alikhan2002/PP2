a=list(input().split())
a=[int(i) for i in a]
j=0
for i in range(1,len(a)):
    if(a[i]>0 and a[j]>0):
        print(a[j],a[i])
        break
    elif(a[i]<0 and a[j]<0):
        print(a[j],a[i])
        break
    j+=1