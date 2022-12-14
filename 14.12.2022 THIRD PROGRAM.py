n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            c=1
if(c==1):
    print("Yes")
else:
    print("No")
            
