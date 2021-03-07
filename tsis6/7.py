s=input()
print("No. of Upper case characters : ", sum(1 for i in s if s.isupper()))
print("No. of Lower case characters : ", sum(1 for i in s if s.islower()))