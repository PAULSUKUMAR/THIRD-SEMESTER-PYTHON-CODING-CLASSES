sno=int(input("Enter sno value:"))
name=input("Enter the Student Name:")
group=input("Enter the group name:")
s1=int(input("marks of subject 1:"))
s2=int(input("marks of subject 2:"))
s3=int(input("marks of subject 3:"))
if s1>35 and s2>35 and s3>35 :
    print(sno,name,group,": PASS")
else:
    print("FAIL")
