# Sum of all elements in an array

arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

total = 0
for i in range(len(arr)):
    total += arr[i]

print("Sum:", total)

## Using in build functions
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)
print("Sum:", sum(arr))