# Find Second Largest in an array

arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

largest = -1
second_largest = -1

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Second Largest:", second_largest)

## Using in build functions
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)
arr = sorted(set(arr))
print("Second Largest:", arr[-2])