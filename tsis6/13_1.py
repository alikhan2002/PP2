def current_row(n):
    row=list()
    for i in range(n):
        if i==0 or i==n-1:
            row.append(1)
        else:
            c_row=current_row(n-1)
            row.append(c_row[i-1]+c_row[i])
    return row
 
def triangle(m):
    result=list()
    for i in range(m):
        result.append(current_row(i+1))
    ### beautify
    for j in result:
        print(j)
n=int(input())
triangle(n)
print(current_row(n))