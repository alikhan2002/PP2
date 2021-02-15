s=str(input())
n=len(s)
cnt=1
for i in range(n):
    if(s[i]==" "):
        cnt+=1
        
print(cnt)