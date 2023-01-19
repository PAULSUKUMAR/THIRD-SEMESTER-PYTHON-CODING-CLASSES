s=input()
n=len(s)
for i in range(n,-1,-1):
    for j in range(i):
        print(s[j],end=' ')
    print()
