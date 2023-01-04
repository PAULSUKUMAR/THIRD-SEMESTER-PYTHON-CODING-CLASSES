n=int(input('Enter num:'))
m=[]
k=[]
for i in range(0,n):
    l=[]
    for j in range(0,n):
        x=int(input('Enter element:'))
        l.append(x)
    m.append(l)
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            k.append(m[i][j])
    
        if i+j==n-1:
             k.append(m[i][j])
        
        
print(k)        
print('Maximum num:',max(k))
