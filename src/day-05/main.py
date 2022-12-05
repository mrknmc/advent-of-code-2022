import itertools
import re


def transpose(table: list[list[str]]) -> list[list[str]]:
    new_table = [['' for _ in table] for _ in table[0]]
    for x, row in enumerate(table):
        for y, _ in enumerate(row):
            if table[x][y].isalpha():
                new_table[y][x] = table[x][y]
    return new_table


def pop(table: list[list[str]], count: int, from_: int, to_: int) -> None:
    popped = [table[from_ - 1].pop() for _ in range(count)]
    table[to_ - 1].extend(popped)


def pop_in_order(table: list[list[str]], count: int, from_: int, to_: int) -> None:
    popped = [table[from_ - 1].pop() for _ in range(count)]
    table[to_ - 1].extend(popped[::-1])


def main():
    lines = (line.rstrip('\n') for line in open('src/day-05/data1.txt', 'r').readlines())
    # read stacks
    stacks = [list(line) for line in itertools.takewhile(lambda l: not l.startswith(' 1'), lines)]

    new_table = transpose(stacks)

    # remove all empties and reverse stacks
    trimmed_stacks = [''.join(row) for row in new_table]
    trimmed_stacks = [list(stack[::-1]) for stack in trimmed_stacks if stack]

    # drop empty line
    next(lines)

    instructions = [re.match(r'^move (\d+) from (\d+) to (\d+)$', line).groups() for line in lines]  # type: ignore

    cloned_stacks = [list(stack) for stack in trimmed_stacks]

    for count, from_, to_ in instructions:
        pop(trimmed_stacks, int(count), int(from_), int(to_))
    
    result = ''.join(stack[-1] for stack in trimmed_stacks)
    print(f'Part 1: {result}')

    for count, from_, to_ in instructions:
        pop_in_order(cloned_stacks, int(count), int(from_), int(to_))
    
    result = ''.join(stack[-1] for stack in cloned_stacks)
    print(f'Part 2: {result}')


if __name__ == '__main__':
    main()