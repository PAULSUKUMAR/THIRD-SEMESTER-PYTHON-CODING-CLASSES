n=int(input("enter n value"))
temp=n
sum=0
while(n>0):
	r=n%10
	sum=(sum*10)+r
	n=n//10
if(temp==sum):
	print("palindrome")
else:
	print("not palindrome")
