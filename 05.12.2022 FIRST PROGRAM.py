n=int(input("enter n value"))
flag=0
for i in range(2,n+1):
	count=0
	for j in range(2,i-1):
		if(i%j==0):
			count=1
			break
	if(count==0):
		flag=flag+1
		print(i)
print("count is",flag)
