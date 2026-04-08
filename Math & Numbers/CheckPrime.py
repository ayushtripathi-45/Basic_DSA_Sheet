num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

## How it works (simple)
## Instead of checking all numbers up to num, we check only up to √num.
## If no number divides it, then it is prime.