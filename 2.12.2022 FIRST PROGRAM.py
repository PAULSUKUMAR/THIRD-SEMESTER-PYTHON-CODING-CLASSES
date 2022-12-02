#WAY 1:

a=int(input())
b=int(input())
def BiggestOfTwo(a,b):
 if(a>b):
  print('a is big')
 else:
  print('b is big')
BiggestOfTwo(a,b)

#WAY 2:

def BiggestOfTwo(a,b):
 if(a>b):
  return "a is big"
 else:
  return "b is big"
a=int(input())
b=int(input())
print(BiggestOfTwo(a,b))

#WAY 3:

def BiggestOfTwo(a,b):
 if(a>b):
  return True
 else:
  return True
a=int(input())
b=int(input())
if(BiggestOfTwo(a,b)):
 print('a is big')
else:
 print('b is big')
