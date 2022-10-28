def palindrome(num):
    n=num
    rev=0
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    if rev==n:
        return True
    else:
        return False
a=int(input())
print(palindrome(a))