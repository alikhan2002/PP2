a=list(input().split())
a=[int(i) for i in a]
cnt=0
for i in range(len(a)):
    if(a[i]>0):
        cnt+=1
print(cnt)