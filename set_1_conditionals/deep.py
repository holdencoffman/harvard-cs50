response = input('What is the answer to the great question of life, the universe, and everything?\n').lower().strip()
if response in ('42', 'forty-two', 'forty two'):
   print('Yes')
else:
   print('No')