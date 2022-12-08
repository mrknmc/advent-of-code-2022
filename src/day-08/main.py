

from itertools import takewhile


def main():
    lines = [l.strip() for l in open("src/day-08/data1.txt", "r").readlines()]
    table = [list(line) for line in lines]

    # circumference
    visible = 2 * len(table) + 2 * len(table[0]) - 4

    for i in range(1, len(table) - 1):
        for j in range(1, len(table[0]) - 1):
            val = table[i][j]
            top = all(table[x][j] < val for x in reversed(range(i)))
            bottom = all(table[x][j] < val for x in range(i+1, len(table)))
            left = all(table[i][y] < val for y in reversed(range(j)))
            right = all(table[i][y] < val for y in range(j+1, len(table[0])))
            if any([top, left, right, bottom]):
                visible += 1

    print(f'Part 1: {visible}')

    max_val = 0
    for i in range(0, len(table)):
        for j in range(0, len(table[0])):
            val = table[i][j]

            top = 0
            for x in reversed(range(i)):
                top += 1
                if table[x][j] >= val:
                    break

            bottom = 0
            for x in range(i+1, len(table)):
                bottom += 1
                if table[x][j] >= val:
                    break

            left = 0 
            for y in reversed(range(j)):
                left += 1
                if table[i][y] >= val:
                    break

            right = 0
            for y in range(j+1, len(table[0])):
                right += 1
                if table[i][y] >= val:
                    break

            visible = top * bottom * left * right
            if visible >= max_val:
                max_val = visible

    print(f'Part 2: {max_val}')



if __name__ == "__main__":
    main()
