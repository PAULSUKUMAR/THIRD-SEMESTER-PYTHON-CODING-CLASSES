n,r=input().split()
n=int(n)
r=int(r)
l=list(map(int,input().split()))
for i in range(0,r):
    f=l[n-1]
    for j in range(n-1,0,-1):
        l[j]=l[j-1]
    l[0]=f
for i in l:
        print(i,end=" ")
