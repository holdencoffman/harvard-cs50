import inflect as inf

def gather_input():
    names = []
    while True:
        try:
            response = input('Please input a name below. Enter Ctrl+D when finished:\n')
            names.append(response)
        except EOFError:
            break
    return names

def build_output(names):
    output_string = 'Adieu, adieu, to '
    p = inf.engine()
    output_string = output_string + p.join(names)
    return output_string

def main():
    names = gather_input()
    output = build_output(names)
    print(output)

if __name__ == '__main__':
    main()