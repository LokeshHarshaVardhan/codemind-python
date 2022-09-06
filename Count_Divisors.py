a,b,x=map(int,input().split())
c=0
for i in range(a,b+1):
    if i%x==0:
        c+=1
print(c)