import math
n=int(input())
t=n
s=0
while n>0:
    r=n%10
    n=n//10
    k=math.factorial(r)
    s+=k
if t==s:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")