# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string=input()
x=re.findall(r"(.)\1\2",string)
if(x):
    print(x[0])
else:
    print("-1")