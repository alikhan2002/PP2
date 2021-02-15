a = list(input().split())
a = [int(i) for i in a]
for i in range(len(a)):
    if(a[i]%2==0):
         print(a[i])