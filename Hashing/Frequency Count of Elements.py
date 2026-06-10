arr = list(map(int, input("Enter elements: ").split()))

freq = {}

for num in arr:

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency Count:")

for key, value in freq.items():
    print(key, "->", value)