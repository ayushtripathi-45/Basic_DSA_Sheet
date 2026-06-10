arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))

seen = {}

found = False

for i in range(len(arr)):

    compl = target - arr[i]

    if compl in seen:
        print("Pair found at indices:",
              seen[compl], "and", i)
        found = True
        break

    seen[arr[i]] = i

if not found:
    print("No pair found")