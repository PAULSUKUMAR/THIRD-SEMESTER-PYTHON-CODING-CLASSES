n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in range(0,n):
    if l[i]%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
l=e+o
print(l)
