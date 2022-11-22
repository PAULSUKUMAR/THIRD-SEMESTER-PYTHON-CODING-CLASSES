P=int(input("Enter Principal Amount:"))
T=int(input("Enter Time pPeriod:"))
R=int(input("Enter Rate Of Intrest:"))
SI=(P*T*R)/100
EMI=(SI+P)/T*12
print("EMI is",EMI)
