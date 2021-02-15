<<<<<<< HEAD
x=int(input())
res=int((x*45)/60)+9
b=int((x-1)/2)*15
b1=int(x/2)*5
res1=int((x*45+b+b1)%60)
m=int(res1/10)
m1=int(res1%10)
txt="{} {}{}"
=======
x=int(input())
res=int((x*45)/60)+9
b=int((x-1)/2)*15
b1=int(x/2)*5
res1=int((x*45+b+b1)%60)
m=int(res1/10)
m1=int(res1%10)
txt="{} {}{}"
>>>>>>> 8ecb3b6086a1bfc36d58a4d7bc880e4cf8fa22b9
print(txt.format(res,m,m1))