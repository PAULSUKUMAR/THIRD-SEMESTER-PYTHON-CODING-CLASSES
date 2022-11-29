empo=int(input("enter empo"))
empname=input("enter name")
basicsalary=int(input("enter basic salary"))
empdesig=input("enter empdesig")
ta=int(input("enter ta"))
da=int(input("enter da"))
hra=int(input("enter hra"))
netsalary=basicsalary+ta+da+hra
print(netsalary)
if (netsalary>100000):
	tax=netsalary*10/100
if (netsalary>50000):
	tax=netsalary*7/100
if(netsalary>40000):
	tax=netsalary*4/100
if(netsalary>20000):
	tax=netsalary*2/100
if(netsalary<20000):
	tax=0
print("tax is",tax)
