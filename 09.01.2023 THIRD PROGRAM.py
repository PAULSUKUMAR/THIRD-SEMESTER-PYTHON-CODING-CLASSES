s=input()
l=[]
for i in s:
    l.append(int(i))
l.sort()
l.reverse()
res=''
for i in l:
    res=res+str(i)
print(res)

