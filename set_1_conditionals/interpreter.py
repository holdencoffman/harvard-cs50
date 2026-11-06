def main():
   expression = input('Please type your arithmetic expression below:\n')
   calculator(expression)

def calculator(expression):
   elements = expression.split(' ')
   operator = elements[1]
   operand_1 = int(elements[0]) 
   operand_2 = int(elements[2])

   if operator == '+':
      result = float(operand_1 + operand_2)
   elif operator == '-':
      result = float(operand_1 - operand_2)
   elif operator == '*':
      result = float(operand_1 * operand_2)
   elif operator == '/':
      result = float(operand_1 / operand_2)

   print(f'{result:.1f}')

if __name__ == '__main__':
   main()