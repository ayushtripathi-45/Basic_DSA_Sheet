# Rotate array to the left

arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

arr = arr[1:] + [arr[0]]

print("Rotated array:", arr)