n=int(input())
m=int(input())
a=[]
b=[]
sum1=0
sum2=0
for i in range(0,n):
    l=[]
    for j in range(0,n):
        x=int(input("enter ele"))
        l.append(x)   
    a.append(l)
for i in range(n):
    for j in range(n):
        if i==j:
            sum1=(sum1+a[i][j])     
print(a)
print(sum1) 
for i in range(0,m):
    k=[]
    for j in range(0,m):
        y=int(input())
        k.append(y)
    b.append(k)    
for i in range(m):
    for j in range(m):
        if i+j==n-1:
            sum2=sum2+b[i][j]
print(b)
print(sum2)
print("difference",sum1-sum2)
