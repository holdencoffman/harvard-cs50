def main():
   variable_name = input('Please provide your camel case variable name below to convert it to snake case:\n')
   print(camel_to_snake(variable_name))

def camel_to_snake(variable_name):
   snake_case = ''
   for char in variable_name:
      if char.islower():
         snake_case = snake_case + char
      elif char.isupper():
         snake_case = snake_case + '_' + char.lower()
   return snake_case

if __name__ == '__main__':
   main()