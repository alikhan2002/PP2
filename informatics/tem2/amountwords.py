def CountWords (s):
    cnt=1
    s =string.casefold() 
    for i in range(len(s)):
        if(s[i]==" " and (s[i-1]>='a' and s[i-1]<='z')):
            cnt+=1
            if(s[i]==" " and not(s[i-1]>='a' and s[i-1]<='z')):
                cnt-=1
        if(i==len(s)-1 and not(s[i]>='a' and s[i]<='z')):
                    cnt-=1          
    print(cnt)


string=str(input())  
CountWords(string)

