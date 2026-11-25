import random as rd

def setup_game():
    response = input('Please inupt a positive integer:\n')
    while not response.isnumeric() or int(response) <= 0:
        response = input('That input was invalid. Please input a positive level:\n')
    response = int(response)
    prize_int = rd.randint(1, response)
    return response, prize_int

def play_game(response, prize_int):
    guess = 0
    while (guess != prize_int):
        guess = input('Please choose a number between 1 and ' + str(response) + '. Guess:\n')
        if not guess.isnumeric():
            continue
        else:
            guess = int(guess)
        if guess < prize_int:
            print('Too small!')
        elif guess > prize_int:
            print('Too large!')
        elif guess == prize_int:
            print('Just right!')

def main():
    response, prize = setup_game()
    play_game(response, prize)

if __name__ == '__main__':
    main()