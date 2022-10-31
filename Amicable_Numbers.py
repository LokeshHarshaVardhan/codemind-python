def amicable(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
a=int(input())
b=int(input())
if amicable(a)==b and amicable(b)==a:
    print('Amicable')
else:
    print("Not Amicable")