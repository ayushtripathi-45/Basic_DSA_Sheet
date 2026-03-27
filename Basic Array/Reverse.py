# Reverse of an array

## Two-pointer approach or iterative swapping.
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)

## Using in-build Functions
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)
arr.reverse()
print("Reversed array:", arr)