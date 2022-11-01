def reverse_integer(n):
    y=str(abs(n))
    y = y[::-1]
    output = int(y)
    if n < 0:
        return -1 * output
    else:
        return output
a=int(input())
print(reverse_integer(a))