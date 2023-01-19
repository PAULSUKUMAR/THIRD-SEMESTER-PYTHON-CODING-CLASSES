def isBalanced(s):
    for i in range(0,n+1):
        while(True):
            if '[]' in s:
                s=s.replace('[]','')
            elif '()' in s:
                s=s.replace('()','')
            elif '{}' in s:
                s=s.replace('{}','')
            else:
                return not s
n=int(input())    
for i in range(0,n,1):
    s=input()
    if isBalanced(s):
        print('YES')
    else:
        print('NO')
