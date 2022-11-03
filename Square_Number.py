n=int(input())
c=0
for i in range(1,n+1):
    if n==i*i:
        c=1
if c==1:
    print('True')
else:
    print('False')