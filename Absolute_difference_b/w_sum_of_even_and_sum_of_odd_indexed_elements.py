n=int(input())
l=list(map(int,input().split()))[:n]
e=0
o=0
for i in range(n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
print(abs(e-o))