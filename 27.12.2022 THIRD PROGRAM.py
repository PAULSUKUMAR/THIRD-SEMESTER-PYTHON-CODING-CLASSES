n=int(input())
l=list(map(int,input().split()))
x=int(input())
low=0
h=n-1
check=0
mid=(low+h)//2
while h>=low:
    if x>l[mid]:
        low=mid+1
    elif x==l[mid]:
        check=1
        break
    else:
        h=mid-1
    mid=(low+h)//2
if check==1:
    print("ele found",mid,"indexvalue")
else:
     print("ele not found")
