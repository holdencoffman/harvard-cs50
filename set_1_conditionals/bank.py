response = input("Write the bank teller's greeting.\n").lower().strip()

if response[:5] == 'hello':
   print('$0')
elif response[0] == 'h':
   print('$20')
else:
   print('$100')