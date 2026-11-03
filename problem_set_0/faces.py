def convert(input):
   return input.replace(':)', '🙂').replace(':(', '🙁')

def main():
   response = input('Type your input below:\n')
   print(convert(response))

main()