def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    

n = int(input("Enter the number whose factorial has to be printed:"))
print(f"The factorial of {n} is:", factorial(n))

