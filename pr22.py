h=int(input())
f=list(map(int,input().split()))
s=sorted(f)
e=s[::-1]
d=e[0]
a=e[1]
print(d+a)
