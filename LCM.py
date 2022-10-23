a, b = map(int, input().split())
if a > b:
    a, b = b, a
i = 1
while 1:
    m = b * i 
    if m % a == 0:
        print(m)
        break
    i+=1