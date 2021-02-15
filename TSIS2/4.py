<<<<<<< HEAD
gain = [-5,1,5,0,-7]
n=len(gain)
ans=0
x=0
for i in range(n):
    x+=gain[i]
    ans=max(ans,x)
=======
gain = [-5,1,5,0,-7]
n=len(gain)
ans=0
x=0
for i in range(n):
    x+=gain[i]
    ans=max(ans,x)
>>>>>>> 8ecb3b6086a1bfc36d58a4d7bc880e4cf8fa22b9
print(ans)