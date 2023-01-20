s=input()
n=len(s)
s=sorted(s)
for i in range(1,n):
    if ord (s[i])-ord(s[i-1])==2:
        continue
    else:
         ch=chr(ord (s[i])+1)
         print(ord(ch),end=' ')
