p=[]
def perfect(x):
    y=1
    while(y!=x):
        y+=1
        if(x%y==0):
            p.append(y)
x=int(input())
