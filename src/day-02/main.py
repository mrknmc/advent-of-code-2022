
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

def main():
    lines = open('src/day-02/data1.txt', 'r').readlines()
    total = 0
    for line in lines:
        [theirs, mine] = line.strip().split(' ')
        match (theirs, mine):
            case 'A', 'X':
                total += 1
                total += 3
            case 'A', 'Y':
                total += 2
                total += 6
            case 'A', 'Z':
                total += 3
            case 'B', 'X':
                total += 1
            case 'B', 'Y':
                total += 2
                total += 3
            case 'B', 'Z':
                total += 3
                total += 6
            case 'C', 'X':
                total += 1
                total += 6
            case 'C', 'Y':
                total += 2
            case 'C', 'Z':
                total += 3
                total += 3

    print(f'Part 1: {total}')

    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

    total = 0
    for line in lines:
        [theirs, mine] = line.strip().split(' ')
        match (theirs, mine):
            case 'A', 'X':
                total += 3
            case 'A', 'Y':
                total += 1
                total += 3
            case 'A', 'Z':
                total += 6
                total += 2
            case 'B', 'X':
                total += 1
            case 'B', 'Y':
                total += 2
                total += 3
            case 'B', 'Z':
                total += 3
                total += 6
            case 'C', 'X':
                total += 2
            case 'C', 'Y':
                total += 3
                total += 3
            case 'C', 'Z':
                total += 1
                total += 6

    print(f'Part 2: {total}') 


if __name__ == '__main__':
    main()