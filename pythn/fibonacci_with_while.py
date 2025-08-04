n = int(input("Enter a number: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print()  # To ensure the output ends with a newline
# This code generates the Fibonacci sequence up to the nth number using a while loop.
