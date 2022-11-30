PN=500
MD=300
BS=200
Mk=280
Ch=380
cphno=input("Enter customer number:")
cname=input("Enter customer name:")
caddr=input("Enter customer address:")
P=int(input("Enter the quantity:"))
M=int(input("Enter the quantity:"))
B=int(input("Enter the quantity:"))
M=int(input("Enetr the quantity:"))
C=int(input("Enter the quantity:"))
bill=(PN*P)+(MD*M)+(BS*B)+(Mk*M)+(Ch*C)
if bill>3000:
    tax=bill*5/100
elif bill>2000:
    tax=bill*7/100
elif bill>1000:
    tax=bill*10/100
elif bill>500:
    tax=bill*15/100
else:
    tax=bill+100
print("customer no",cphno)
print("customer name",cname)
print("tax",tax)
print("bill",bill)
print("total amount",bill+tax)
