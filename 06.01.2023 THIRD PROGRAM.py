email=input("enter email:")
phn=input("enter phn no:")
if email.endswith("@gmail.com")or email.endswith("@yahoo.com") or email.endswith("@adc.aditya.ac.in") and (len(phn)==10) and phn.startswith("9") or phn.startswith("8") or phn.startswith("7") or phn.startswith("6"):
    print("registration successfully")
else:
    print("check details")
