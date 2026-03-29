# To check string Palindrome of not

## Using Loop and Comparision
s = input("Enter string: ")

n = len(s)
is_palindrome = True

for i in range(n):
    if s[i] != s[n - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")

## Using Slicing method
s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")