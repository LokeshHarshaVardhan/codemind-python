n=int(input())
for i in range(n):
    l=int(input())
    t=l
    rev=0
    while l>0:
        r=l%10
        l=l//10
        rev=rev*10+r
    if t==rev:
        print('True')
    else:
       print('False')