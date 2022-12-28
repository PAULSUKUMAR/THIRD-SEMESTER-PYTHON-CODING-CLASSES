n=int(input())
l=list(map(int,input("Enter Numbers:").split()))
start=n//2
stop=n-1
while(start<stop):
    l[start],l[stop]=l[stop],l[start]
    start+=1
    stop-=1
print(l)
