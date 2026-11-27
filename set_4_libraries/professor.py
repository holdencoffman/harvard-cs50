import random as rd

def get_level():
    level = input('Please choose a level between 1 and 3. Level:\n')
    while not level.isnumeric() or int(level) not in list(range(1,4)):
        print('That input was invalid, try again.')
        level = input('Please choose a level between 1 and 3. Level:\n')
    return int(level)

def generate_integer(level):
    if level not in list(range(1,4)):
        raise ValueError('Level must be between 1 and 3.')
    else:
        num = rd.randint((10 ** (level - 1)) if level > 1 else 0, (10 ** level) - 1)
        return num

def build_problem(level):
    problem_list = []
    for i in range(3):
        if i < 2:
            problem_list.append(generate_integer(level))
        else:
            problem_list.append(problem_list[0] + problem_list[1])
    return problem_list

def main():
    level = get_level()
    win_count = 0
    for i in range(10):
        problem_list = build_problem(level)
        for i in range(3):
            prompt = f'{problem_list[0]} + {problem_list[1]} = '
            answer = input(prompt)
            if (not answer.isnumeric() or int(answer) != problem_list[2]):
                if i < 2:
                    print('EEE')
                    continue
                else:
                    print(f'The correct answer was {problem_list[2]}')
                    break
            else:
                win_count += 1
                break
    print(win_count)

if __name__ == '__main__':
    main()