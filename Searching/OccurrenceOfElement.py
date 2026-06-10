arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter element to count: "))

count = 0

for num in arr:
    if num == target:
        count += 1

print("Occurrences:", count)