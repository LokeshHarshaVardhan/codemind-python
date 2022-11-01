n=int(input())
c=0
rev=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
s=0
for j in range(1,rev+1):
        if rev % j==0:
            s+=1
if c==2 and s==2:
    print("circular prime")
elif c==2:
    print('prime but not a circular prime')
else:
    print('not prime')