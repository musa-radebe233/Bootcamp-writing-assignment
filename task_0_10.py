def common_letters(var1, var2):
   s1 = set(var1)
   s2 = set(var2)
   words = list(s1 & s2)
   print("Common letters:",end = ' ')
   for i in words:
      if i in words and i != empty_string.upper():
         print(i.lower(), end =', ')  
common_letters("house","mouse")


