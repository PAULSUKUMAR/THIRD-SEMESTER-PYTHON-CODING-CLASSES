n=int(input())
l=list(map(int,input().split()))
x=int(input())
r=[]
c=0
for i in range(0,n):
    if x==l[i]:
        print("Element is found at index",i)
        c=c+1
if c==0:
    print("Element is not found")

        
