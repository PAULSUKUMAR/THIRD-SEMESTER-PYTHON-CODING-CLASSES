#WAY 1:
def age(a):
 if(a>=18):
  print('yes')
 else:
  print('no')
a=int(input('enter age'))
age(a)

#WAY 2:

def age(a):
 if(a>=18):
  return 'yes'
 else:
  return 'no'
a=int(input('enter age'))
print(age(a))

#WAY 3:

def age(a):
 if(a>=18):
  return True
 else:
  return False
a=int(input('enter age'))
if((age(a))):
 print('yes')
else:
 print('no')
