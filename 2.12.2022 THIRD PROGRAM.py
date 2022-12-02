#WAY 1:
def leap(y):
 if((y%4==0and y%100!=0)or(y%400==0)):
  print('yes')
 else:
  print('no')
y=int(input())
leap(y)
  
#WAY 2:
def leap(y):
 if((y%4==0and y%100!=0)or(y%400==0)):
  return 'yes'
 else:
  return 'no'
y=int(input())
print(leap(y))
#WAY 3:
def leap(y):
 if((y%4==0and y%100!=0)or(y%400==0)):
  return True
 else:
  return False
y=int(input())
if((leap(y))):
 print('yes')
else:
 print('no')
