s=input()
d=''
n=len(s)
for i in range(0,n):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        s.replace(s[i],'')
    elif s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
        s.replace(s[i],' ')
    else:
        d=d+s[i]
print(d)
