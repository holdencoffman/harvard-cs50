def main():
   time = input('Please input the 24-hour time in HH:MM format below.\n')
   time_num = convert(time)
   if 7 <= time_num <= 8:
      print('breakfast time')
   elif 12 <= time_num <= 13:
      print('lunch time')
   elif 18 <= time_num <= 19:
      print('dinner time')

def convert(time):
   time_parts = time.split(':')
   hour = int(time_parts[0])
   min = int(time_parts[1])
   return float(hour + min / 60)

if __name__ == '__main__':
   main()