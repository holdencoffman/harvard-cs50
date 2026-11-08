def main():
   plate_name = input('Please input your license plate name below to check for its validity:\n')
   if is_valid(plate_name):
      print('Valid')
   else:
      print('Invalid')

def is_valid(plate_name):
   validity = True
   # must start with two letters
   if not plate_name[:2].isalpha():
      validity = False
   # must be between 2 and 6 characters
   elif not 2 <= len(plate_name) <= 6:
      validity = False
   # numbers must be all at the end, after letters. first number canot be 0
   elif not numeric_checks(plate_name):
      validity = False
   # no periods, spaces, or punctuation
   elif not plate_name.isalnum():
      validity = False
   return validity

def numeric_checks(plate_name):
   validity = True
   num_numeric = 0
   last_was_numeric = False
   for char in plate_name:
      # verify first numeric char, if present, is not 0
      if char == '0' and num_numeric == 0:
         validity = False
         break
      if char.isnumeric():
         num_numeric += 1
         last_was_numeric = True
      # if preceding char was numeric, and this char flips back to alphabetic
      elif last_was_numeric:
         validity = False
         break
   return validity

if __name__ == '__main__':
   main()