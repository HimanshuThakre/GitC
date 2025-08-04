def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter a number: "))
for i in range(n):
    print(fibonacci(i), end=' ')
print()  # To ensure the output ends with a newline
# This code generates the Fibonacci sequence up to the nth number using recursion.

    