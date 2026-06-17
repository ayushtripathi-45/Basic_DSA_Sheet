# Remove Duplicates from am array

## Two-pointer approach
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

left = 0
for right in range(1, len(arr)):
    if arr[right] != arr[left]:
        left += 1
        arr[left] = arr[right]

arr = arr[:left+1]

print("After removing duplicates:", arr)


## Using in build functions
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)
arr = list(set(arr))
print("After removing duplicates:", arr)