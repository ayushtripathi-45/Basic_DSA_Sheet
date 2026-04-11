## Iterative Approach

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
print(find_gcd(48, 18))  # Output: 6

## Recursive Approach

def find_gcd_recursive(a, b):
    if b == 0:
        return a
    return find_gcd_recursive(b, a % b)

# 1. Get input (convert to int immediately)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# 2. Calculate
result = find_gcd_recursive(num1, num2)

# 3. Output
print("The GCD is:", result)