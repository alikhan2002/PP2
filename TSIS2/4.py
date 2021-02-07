gain = [-5,1,5,0,-7]
n=len(gain)
ans=0
x=0
for i in range(n):
    x+=gain[i]
    ans=max(ans,x)
print(ans)