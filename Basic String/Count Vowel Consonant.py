def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0
    other_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1 
        elif char.isalpha():
            consonant_count += 1
        else:
            other_count += 1

    return vowel_count, consonant_count, other_count


# User input
text = input("Enter a string: ")
v, c, o = count_vowels_consonants(text)

print(f"\nString     : {text}")
print(f"Vowels     : {v}")
print(f"Consonants : {c}")
print(f"Others     : {o}")
