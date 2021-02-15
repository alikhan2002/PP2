<<<<<<< HEAD
command = "G()(al)"
s=""
for i in range(len(command)):
    if(command[i]=='G'):
        s+='G'
    elif(command[i]=='(' and command[i+1]==')'):
        s+='o'
    elif(command[i]=='(' and command[i+1]=='a'and command[i+2]=='l'and command[i+3]==')'):
        s+="al"
=======
command = "G()(al)"
s=""
for i in range(len(command)):
    if(command[i]=='G'):
        s+='G'
    elif(command[i]=='(' and command[i+1]==')'):
        s+='o'
    elif(command[i]=='(' and command[i+1]=='a'and command[i+2]=='l'and command[i+3]==')'):
        s+="al"
>>>>>>> 8ecb3b6086a1bfc36d58a4d7bc880e4cf8fa22b9
print(s)