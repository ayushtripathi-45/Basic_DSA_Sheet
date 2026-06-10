arr = list(map(int, input("Enter elements: ").split()))

prefsum = 0
seen = set()

found = False

for num in arr:

    prefisum += num

    if prefsum == 0 or prefsum in seen:
        found = True
        break

    seen.add(prefsum)

if found:
    print("Subarray with zero sum exists")
else:
    print("No such subarray")