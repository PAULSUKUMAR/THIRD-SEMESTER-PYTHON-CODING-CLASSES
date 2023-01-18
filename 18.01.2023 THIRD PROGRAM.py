string=input()
l=[]
l[:0]=string
n=len(l)
for i in range(0,n+1):
    for j in range(0,i):
        print(l[j],end='')
    print()
