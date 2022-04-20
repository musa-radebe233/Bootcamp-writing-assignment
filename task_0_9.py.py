# Task 0.9
def vowel(text):
    vowels = ["a","e","i","o","u"]
    i = [letter for letter in text.lower()if letter in vowels]
    print("Vowels:", ",".join(i))
vowel("alike")
