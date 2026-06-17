# Minimum and Maximum in an array

## Iteration through the array.
n = int(input("Array size: "))
arr = []

for i in range(n):
    num = int(input(f"Element {i+1}: "))
    arr.append(num)

max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max:", max_val)
print("Min:", min_val)


## Using in build functions
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)
print("Max:", max(arr))
print("Min:", min(arr))