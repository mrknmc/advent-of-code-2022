def main():
    lines = open("src/day-01/data1.txt", "r").readlines()
    total = 0
    max = 0
    totals = []
    for line in lines:
        if line == "\n":
            totals.append(total)
            if total >= max:
                max = total
            total = 0
        else:
            total += int(line)

    print(f"Part 1: {max}")

    sorted_totals = sorted(totals)

    print(f"Part 2: {sum(sorted_totals[-3:])}")


if __name__ == "__main__":
    main()
