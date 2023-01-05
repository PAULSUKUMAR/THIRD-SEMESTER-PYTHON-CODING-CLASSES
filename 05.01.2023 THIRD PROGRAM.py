n=int(input('Enter number:'))
l=list(map(int,input().split()))
s=int(input('Enter s:'))
l.sort()
m=l[-s:]
print('Maximun number:',max(l))
print('Minuimum number:',min(l))
print('DIfference:',max(m)-min(m))
