n=int(input('Enter num:'))
m=[]
c=0
for i in range(0,n):
    l=[]
    for j in range(0,n):
        x=int(input('Enter ele:'))
        l.append(x)
    m.append(l)
for i in range(0,n):
    sum=0
    for j in range(0,n):
        sum=sum+m[i][j]
    if sum==2:
        c=c+1
if c==3:
    print('Coder target matrix')
else:
    print('not a coder target matrix')
