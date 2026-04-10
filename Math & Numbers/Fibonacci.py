## Recursive Method
def fib_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Input
n_terms = int(input("Enter number of terms: "))

# Output
fib_series = [fib_recursive(i) for i in range(n_terms)]
print(fib_series)

## Iterative Approach
# Input
n_terms = int(input("Enter number of terms: "))

a, b = 0, 1
fib_series = []

for _ in range(n_terms):
    fib_series.append(a)
    a, b = b, a + b  # The simultaneous update

# Output
print(fib_series)