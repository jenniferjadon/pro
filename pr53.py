b=input()
s=[]
for i in b:
    if i!=' ':
        if i not in s:
            l=i.lower()
            s.append(l)
if len(s)==26:
    print("yes")
else:
    print("no")
        
