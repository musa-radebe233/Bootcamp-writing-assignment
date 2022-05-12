def common_letters(var1, var2):
  var1 = var1.lower()
  var2 = var2.lower()
  words = (set(var1) & set(var2))
  letters = (letter for letter in words)
  letters_2 = ",".join(letters)
  print(f"Common letters: {letters_2}") 
common_letters("house","mouse")


