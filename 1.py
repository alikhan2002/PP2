import re
txt = "Che to tam"
x=re.findall("tot", txt)
if(x):
    print("GOOD JOB\n", x)
else:
    print("BAD JOB")