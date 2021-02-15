a = list(input().split())
a = [int(i) for i in a]
for i in range(len(a)):
    if(int(i)%2==0):
         print(a[i])