def sum_of_digits(n):
    total = 0
    # Handle negative numbers by taking absolute value
    n = abs(n)
    
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n = n // 10
        
    return total

# Example usage:
num = 1234
print(f"The sum of digits of {num} is {sum_of_digits(num)}") 
# Output: 10