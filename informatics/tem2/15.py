<<<<<<< HEAD
a=int(input())
h=int((a/3600)%24)
m1=int(((a/60)%60)/10)
m=int(((a/60)%60)%10)
s=int((a%60)/10)
s1=int((a%60)%10)
res="{}:{}{}:{}{}"
=======
a=int(input())
h=int((a/3600)%24)
m1=int(((a/60)%60)/10)
m=int(((a/60)%60)%10)
s=int((a%60)/10)
s1=int((a%60)%10)
res="{}:{}{}:{}{}"
>>>>>>> 8ecb3b6086a1bfc36d58a4d7bc880e4cf8fa22b9
print(res.format(h,m1,m,s,s1))