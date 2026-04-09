## Iterative Approach (Using a Loop)

num = int(input("Enter a number: "))

def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"The factorial of {num} is: {factorial_iterative(num)}")

## Recursive Approach

num = int(input("Enter a number: "))

def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)

print(f"The factorial of {num} is: {factorial_recursive(num)}")