# Reverse an integer without using built-in reverse functions

n = int(input("Enter an integer: "))

reverse = 0

while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reversed integer:", reverse)