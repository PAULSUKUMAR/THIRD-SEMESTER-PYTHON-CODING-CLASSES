s=input()
m=int(input())
res=''
n=len(s)
for i in range(0,n):
    for j in range(0,m):
        res=res+s[i]
print(res)
