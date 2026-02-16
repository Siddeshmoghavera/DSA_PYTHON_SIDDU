# Using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")


# Using Iteration
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("Enter number of terms: "))
fibonacci(n)
