a=list(input().split())
a=[int(i) for i in a]
sum=1
for i in range (len(a)):
  sum*=a[i]
print(sum)