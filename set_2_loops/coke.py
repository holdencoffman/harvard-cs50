def main():
   change = vending()
   print('Change Owed:', change)

def vending():
   balance = 0
   while balance < 50:
      coin = int(input('Please insert either a quarter, a dime, or a nickel by typing the cents below:\n'))
      if coin in [5, 10, 25]:
         balance += coin
      if balance < 50:
         print('Amount Due:', 50 - balance)
   return max(0, balance - 50)


if __name__ == '__main__':
   main()