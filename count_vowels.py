text = input("Enter a string: ").lower()  # Convert whole string to lowercase
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels in the string:", count)
"""
text = input("Enter a string: ").lower()  # Make input lowercase
vowels = "aeiou"
vowel_counts = {v: 0 for v in vowels}     # Dictionary to store counts

# Count each vowel
for ch in text:
    if ch in vowels:
        vowel_counts[ch] += 1

# Print individual vowel counts
for v in vowels:
    print(f"{v} : {vowel_counts[v]}")

# Print total vowels
total = sum(vowel_counts.values())
print("Total number of vowels:", total)

"""