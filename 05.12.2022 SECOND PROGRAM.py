n=int(input("enter n number"))
g=n
s=n
for i in range(n):
	n=int(input("enter numbers"))
	if n>g:
		g=n
	if n<s:
		s=n
print("the difference is",g-s)
print("largest number is",g)
print("smallest number is",s)
