n=int(input('Enter num:'))
l=list(map(int,input().split()))
for i in range(0,n):
       if l[i]%2!=0:
           print(l[i],end=' ')
