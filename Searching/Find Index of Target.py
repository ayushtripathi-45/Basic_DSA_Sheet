arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target: "))

index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print("Index:", index)