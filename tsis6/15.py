import re
s=input()
x=re.findall(r'[a-z]*',s)
x.sort()
t=list(filter(lambda e: e!='', x))
g='-'.join(t)
for i in g:
    print(i,end='')