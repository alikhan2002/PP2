a=list(input().split())
a=[int(i) for i in a]
b=list(input().split())
b=[int(i) for i in b]
ss=set(a)
s=set(b)
res=set.intersection(ss,s)
r=list(res)
r.sort()
for i in range(len(r)):
    print(r[i])