# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
x=input()
y=input()
txt=re.search(r'y',x)
s=txt.start()
print(s)