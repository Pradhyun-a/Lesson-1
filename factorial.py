def factorial(m):
    if m==0 or m==1:
        return 1
    else:
        return m * factorial (m - 1)
print(factorial(10))
