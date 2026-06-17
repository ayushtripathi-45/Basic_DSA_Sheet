s = input("Enter a string: ")

for i in range(len(s)):
    found = False
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            found = True
            break
    if not found:
        print("First non-repeating character:", s[i])
        break
else:
    print("No non-repeating character found")