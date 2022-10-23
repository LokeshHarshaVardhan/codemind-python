n=int(input())
l=n*n
k=str(l)
c=0
while n>0:
    r=n%10
    c+=1
    n=n//10
s=int(k[-c:])
if s==l**0.5:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")