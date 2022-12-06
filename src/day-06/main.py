

def main():
    text = open('src/day-06/data1.txt', 'r').read()
    texts = [text[i:] for i in range(4)]
    i = 0
    for i, chars in enumerate(zip(*texts)):
        if len(set(chars)) == 4:
            break

    print(f'Part 1: {i+4}')

    texts = [text[i:] for i in range(14)]
    i = 0
    for i, chars in enumerate(zip(*texts)):
        if len(set(chars)) == 14:
            break

    print(f'Part 1: {i+14}')


if __name__ == '__main__':
    main()