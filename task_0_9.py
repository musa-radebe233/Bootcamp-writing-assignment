def vowel(text):
    vowels = ["a","e","i","o","u"]
    d = ""
    for i in text:
        if i not in d:
            d = d + i
    for i in d:
        if i in vowels and i != d.upper():
            print(",", i, end = '')
vowel(list("Umuzii"))




