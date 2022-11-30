



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
coupon=input("ENTER COUPON CODE IN CAPITAL LETTERS:")
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
if coupon =='DIWALI' and bill>=5000:
    dis=bill*10/100
elif coupon=='DIWALI' and bill>=3000:
    dis=bill*6/100
elif coupon=='DIWALI' and bill>=1000:
    dis=bill*4/100
else:
    dis=0
if coupon =='CHRISMAS' and bill>=3000:
    dis=bill*20/100
elif coupon=='CHRISMAS' and bill>=2000:
    dis=bill*10/100
elif coupon=='CHRISMAS' and bill>=1000:
    dis=bill*5/100
else:
    dis=0
    
print('bill without tax:',bill)
print('tax:',tax)
print('Discount:',dis)
bill=bill+tax-dis
print('Customer phonenumber:',cphno)
print('Customer Name:',cname)
print('Customer address:',caddr)
print('Bill amount:',bill)
