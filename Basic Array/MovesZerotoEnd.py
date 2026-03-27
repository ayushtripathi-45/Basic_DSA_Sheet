# Move zeroes to the end of the array

arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

left = 0
for right in range(len(arr)):
    if arr[right] != 0:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1

print("After moving zeroes:", arr)