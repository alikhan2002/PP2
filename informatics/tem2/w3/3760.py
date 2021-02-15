x=int(input())
d={}
for i in range(x):
    f,s=input().split()
    d[f]=s
    d[s]=f
print(d[input()])