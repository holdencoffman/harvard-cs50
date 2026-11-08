def main():
   expression = input('List your name below to have its vowels removed:\n')
   print(vowel_dropper(expression))

def vowel_dropper(expression):
   replacement = ''
   for char in expression:
      if char.lower() not in 'aeiou':
         replacement += char
   return replacement

if __name__ == '__main__':
   main()