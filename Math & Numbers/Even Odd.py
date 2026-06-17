## By using %

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

## By using //

num = int(input("Enter a number: "))

if (num // 2) * 2 == num:
    print("Even")
else:
    print("Odd")