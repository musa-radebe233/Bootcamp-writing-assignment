def vowel(text):
    vowels = ["a","e","i","o","u"]
    d = ""
    print("Vowels:", end = '')
    for i in text:
        if i in vowels and i != d.upper():
            print(i, end = ' ,')
vowel(list("Umuzi"))




