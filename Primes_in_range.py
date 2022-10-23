def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
m=int(input())
n=int(input())
cn=0
for i in range(m,n+1):
    if prime(i):
        cn+=1
print(cn)   