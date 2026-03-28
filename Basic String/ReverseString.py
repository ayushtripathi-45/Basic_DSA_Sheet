# Reverse a string

s = input("Enter a string: ")

reversed_s = ""
for i in range(len(s) - 1, -1, -1):
    reversed_s = reversed_s + s[i]

print(reversed_s)

## Using inbuild function
s = input("Enter a string: ")
print(s[::-1])