def maxi(x,y):
    if(x>y):
        return x
    else:
        return y
def maxi1(x,y,z):
    return maxi(x,maxi(y,z))

x=int(input())
y=int(input())
z=int(input())
print(maxi1(x,y,z))