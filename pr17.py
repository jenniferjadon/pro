o,q=list(map(int,input().split()))
h=list(map(int,input().split()))
c=0
for i in range(0,len(h)):
    for j  in range(1,len(h)):
      if h[i]+h[j]==q:
          c=c+1
          break
      break
if c>=1:
    print("yes")
else:
    print("no")
    
