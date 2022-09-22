n=int(input())
rev=0
s=n**2
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
l=rev**2
a=0
while l>0:
    k=l%10
    l=l//10
    a=a*10+k
if a==s:
    print("True")
else:
    print("False")