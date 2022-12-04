
def main():
    lines = [line.strip() for line in open('src/day-04/data1.txt', 'r').readlines()]
    total = 0
    for line in lines:
        first, second = line.split(',')
        first, second = [int(num) for num in first.split('-')], [int(num) for num in second.split('-')]
        if first[0] >= second[0] and first[1] <= second[1]:
            total += 1
        elif second[0] >= first[0] and second[1] <= first[1]:
            total += 1

    print(f'Part 1: {total}')


    total = 0
    for line in lines:
        first, second = line.split(',')
        first, second = [int(num) for num in first.split('-')], [int(num) for num in second.split('-')]
        if second[0] <= first[0] <= second[1]:
            total += 1
        elif second[0] <= first[1] <= second[1]:
            total += 1
        elif first[0] <= second[0] <= first[1]:
            total += 1
        elif first[0] <= second[1] <= first[1]:
            total += 1

    print(f'Part 2: {total}')


if __name__ == '__main__':
    main()