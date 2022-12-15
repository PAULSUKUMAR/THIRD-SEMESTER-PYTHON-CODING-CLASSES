num=int(input())
l=list(map(int,input().split()))
p=[]
n=[]
for i in range(0,num):
    if l[i]>=0:
        p.append(l[i])
    else:
        n.append(l[i])
l=p+n
print(l)
