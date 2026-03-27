# Rotate array to Right

## Basic array manipulation.
arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

print("Original array:", arr)

n = len(arr)
k = k % n

arr = arr[n-k:] + arr[:n-k]

print("Rotated array:", arr)