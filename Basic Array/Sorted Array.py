# Find Array is sorted or not

## Iteration through the array.
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

print("Sorted" if is_sorted else "Not Sorted")


## Using in build functions
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)
print("Sorted" if arr == sorted(arr) else "Not Sorted")