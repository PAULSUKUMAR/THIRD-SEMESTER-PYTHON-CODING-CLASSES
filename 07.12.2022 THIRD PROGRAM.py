def sumofnumber(n):
    s=0
    while(n!=0):
        r=n%10
        s=s+(r*r)
        n=n//10
    return s
n=int(input())
while(n>9):
    n=sumofnumber(n)
if n==1 or n==7:
    print('happy number')
else:
    print('not a happy number')
