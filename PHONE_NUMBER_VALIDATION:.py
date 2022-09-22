n=int(input())
c=0
while n>0:
    r=n%10
    c+=1
    n=n//10
k=str(n)
z=k[:1]
if c==10 and int(z)==0:
    print('Valid')
else:
    print('Invalid')