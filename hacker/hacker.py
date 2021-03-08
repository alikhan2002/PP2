import re
inp=int(input())
for i in range(inp):
    b=input()
    x=re.findall("^(\+|-|\.|\d*)(\d+|\.)(\d+|\n|\.)(\d)+$",b)
    if(x):
        print("True")
    else:
        print("False")