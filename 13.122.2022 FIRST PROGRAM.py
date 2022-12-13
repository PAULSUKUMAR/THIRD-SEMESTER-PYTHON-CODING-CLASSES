l=[]
n=int(input("Enter n:"))
for i in range(1,n+1):
    d=list(input("Enter district: ").split())
    l.append(d)
l.sort()
print(l)
