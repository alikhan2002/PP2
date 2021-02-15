x=int(input())
y=int(input())
for i in range(x):
    a=list(input().split())
    a=[int(j) for j in a]

for i in range(y):
    b=list(input().split())
    b=[int(j) for j in b]

# res=[]
# for i in range(x+y):
#     for j in range(x):
#         if(a[i]==b[j]):
#             res.append(a[i])
#             a.remove(a[i])
#             b.remove(a[i])
#             continue
ss=set(a)
s=set(b)
res=set.intersection(ss,s)
r=list(res)
r.sort()
for i in range(len(r)):
    print(r[i])
# print(len(res))
# for i in range(len(res)):
#     print(res[i],end=" ")
# print(len(a))
# for i in range(len(a)):
#     print(a[i],end=" ")
# print(len(b))
# for i in range(len(b)):
#     print(b[i],end=" ")
