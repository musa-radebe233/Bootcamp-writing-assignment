# Task 0.9
def vowel(text):
    vowels = "aeiou"
    i = [letter for letter in text.lower()if letter in vowels]
    print("Vowels:")
    print(i)
vowel (input("Enter any word:"))