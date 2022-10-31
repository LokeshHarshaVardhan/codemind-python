n=int(input())
l=list(map(int,input().split()))[:n]
e=0
for i in l:
    if i%2==0:
        e+=i
print(e)