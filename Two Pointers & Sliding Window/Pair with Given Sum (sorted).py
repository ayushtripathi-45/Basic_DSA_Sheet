arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target sum: "))

left = 0
right = len(arr) - 1

found = False

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print(f"Pair found: ({arr[left]}, {arr[right]})")
        found = True
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

if not found:
    print("No pair found")