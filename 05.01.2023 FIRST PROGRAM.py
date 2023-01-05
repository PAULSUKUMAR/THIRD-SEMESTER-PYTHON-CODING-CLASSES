n=int(input('Enter num:'))
m=[]
for i in range(0,n):
    l=[]
    for j in range(0,n):
        x=int(input('Enter elements:'))
        l.append(x)
    m.append(l)
s=int(input('Enter number:'))
for i in range(0,n):
    for j in range(0,n):
        if i+j==n-1:
            m[i][j]=s
        else:
            m[i][j]=0
for i in m:
    print(i)
