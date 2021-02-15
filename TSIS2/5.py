<<<<<<< HEAD
n=int(input())
x=1
y=0
i=0
j=1
while(i<len(str(n))):
    z=int((n/j))%10
    j*=10
    x*=z
    y+=z
    i+=1
=======
n=int(input())
x=1
y=0
i=0
j=1
while(i<len(str(n))):
    z=int((n/j))%10
    j*=10
    x*=z
    y+=z
    i+=1
>>>>>>> 8ecb3b6086a1bfc36d58a4d7bc880e4cf8fa22b9
print(x-y)