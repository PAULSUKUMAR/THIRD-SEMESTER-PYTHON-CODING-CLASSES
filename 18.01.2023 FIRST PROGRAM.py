def convertime(s):
    h=int(s[0:2])
    if s[8]=='A':
        if h==12:
            return '00'+s[2:8]
        else:
            return s[0:8]
    elif s[8]=='P':
        if h==12:
            return s[0:8]
        else:
            h=h+12
            return str(h)+s[2:8]
            
s=input()
print(convertime(s))
