n=int(input())
s=list(str(n))
se=set(str(n))
if len(se)==len(s):
    print('Unique Number')
else:
    print("Not Unique Number")