def rotate(r,n):
    return r[n:]+r[:n]
a=list(input().split())
a=[int (i) for i in a]
x=int(input())
if(x>0):
    rotate(a,x)
elif(x<0):
    rotate(a,-x)
print(a)
