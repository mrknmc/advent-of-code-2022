def main():
    lines = [line.strip() for line in open("src/day-03/data1.txt", "r").readlines()]
    total = 0
    for line in lines:
        first, second = set(line[: len(line) // 2]), set(line[len(line) // 2 :])
        intersection = (first & second).pop()
        total += (
            ord(intersection) - 38 if intersection.isupper() else ord(intersection) - 96
        )

    print(f"Part 1: {total}")

    total = 0
    for (r1, r2, r3) in zip(*(iter(lines),) * 3):
        intersection = (set(r1) & set(r2) & set(r3)).pop()
        total += (
            ord(intersection) - 38 if intersection.isupper() else ord(intersection) - 96
        )

    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()
