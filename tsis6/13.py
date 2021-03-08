def curr(n):
    row=[]
    for i in range(n):
        if(i==0 or i==n-1):
            row.append(1)
        else:
            line=curr(n-1)
            row.append(line[i-1]+line[i])
    return row
    
def tri(n):
    pascal=[]
    for i in range(n):
        pascal.append(curr(i+1))
    for i in pascal:
        print(i)


n=int(input())
tri(n)