#Print N to 1 using Recursion

def print_1_to_n(n):

    if n == 0:
        return

    print_1_to_n(n - 1)
    print(n)

n = int(input("Enter n: "))

print_1_to_n(n) 


# Print N to 1 using Recursion

def print_n_to_1(n):

    if n == 0:
        return

    print(n)
    print_n_to_1(n - 1)

n = int(input("Enter n: "))

print_n_to_1(n)