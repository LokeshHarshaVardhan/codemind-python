a=int(input())
b=int(input())
for n in range(a,b+1):
    
    s=n
    c=0
    l=len(str(n))
    while n!=0:
        r=n%10
        n=n//10
        if r==0 or s==0:
            break
        elif s%r==0:
            c+=1
    if c==l:
        print(s,end=' ')