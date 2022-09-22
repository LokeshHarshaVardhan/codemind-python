import math
n=int(input())
for i in range(n):
    m=int(input())
    s=math.sqrt(m)
    if m%s==0:
        print("True")
    else:
        print("False")