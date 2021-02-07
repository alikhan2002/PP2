address=str(input())
i=0
while i<len(address):
    if address[i]==".":
        print("[.]", end="")
    else:
        print(address[i],end="")
    i+=1