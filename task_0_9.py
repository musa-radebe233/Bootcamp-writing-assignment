def vowel(text):
    vowels = ["a","e","i","o","u"]
    empty_string = ""
    print("Vowels:", end = ' ')
    for i in text:
        if i in vowels and i != empty_string.upper():
            print(i, end = ', ')
vowel("Umuzi")




