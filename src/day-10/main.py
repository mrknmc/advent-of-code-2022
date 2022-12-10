def main():
    lines = [l.strip() for l in open("src/day-10/data1.txt", "r").readlines()]
    cycles = 0
    total_strength = 0
    x = 1
    for line in lines:
        if cycles == 20 or (cycles - 20) % 40 == 0:
            total_strength += cycles * x
        match line.split():
            case ["noop"]:
                cycles += 1
            case ["addx", n]:
                cycles += 1
                if cycles == 20 or (cycles - 20) % 40 == 0:
                    total_strength += cycles * x
                cycles += 1
                x += int(n)

    if cycles == 20 or (cycles - 20) % 40 == 0:
        total_strength += cycles * x

    print(f"Part 1: {total_strength}")

    crt = [['0'] * 40 for _ in range(6)]

    cycles = 0
    x = 1
    for line in lines:
        i = cycles // 40
        j = cycles % 40
        crt[i][j] = '#' if x - 1 <= j <= x + 1 else '.'
        match line.split():
            case ["noop"]:
                cycles += 1
            case ["addx", n]:
                # 1st cycle
                cycles += 1
                # 2nd cycle
                i = cycles // 40
                j = cycles % 40
                crt[i][j] = '#' if x - 1 <= j <= x + 1 else '.'
                cycles += 1
                x += int(n)
            case _:
                raise ValueError(f'Unknown line {line}')

    print('Part 2:')

    for row in crt:
        print(''.join(row))

if __name__ == "__main__":
    main()
