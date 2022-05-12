def vowel(text):
   vowels = "aeiou"
    words = set(vowel for vowel in text.lower() if vowel in vowels)
    letters = ",".join(words)
    print(f" Vowels: {letters}")
vowel("Umuzi")




