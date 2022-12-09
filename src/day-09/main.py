import os
from time import sleep


def main():
    lines = [l.strip() for l in open("src/day-09/data1.txt", "r").readlines()]
    head = (0, 0)
    tail = (0, 0)

    visited: set[tuple[int, int]] = {tail}
    for line in lines:
        direction, length = line.split()
        length = int(length)
        match direction:
            case "U":
                vec = (-1, 0)
            case "D":
                vec = (1, 0)
            case "L":
                vec = (0, -1)
            case "R":
                vec = (0, 1)
            case _:
                raise ValueError(f"Unknown direction {direction}")

        for _ in range(length):
            visited.add(tail)
            head = head[0] + vec[0], head[1] + vec[1]
            match head[0] - tail[0], head[1] - tail[1]:
                case (2, 0) | (-2, 0) | (0, 2) | (0, -2):
                    tail = tail[0] + vec[0], tail[1] + vec[1]
                case x, y if abs(x) > 1 or abs(y) > 1:
                    tail = tail[0] + (1 if x > 0 else -1), tail[1] + (
                        1 if y > 0 else -1
                    )

    print(f"Part 1: {len(visited)}")

    head = (0, 0)
    tails: list[tuple[int, int]] = [(0, 0)] * 9
    visited: set[tuple[int, int]] = {tails[8]}
    for line in lines:
        direction, length = line.split()
        length = int(length)
        match direction:
            case "U":
                vec = (-1, 0)
            case "D":
                vec = (1, 0)
            case "L":
                vec = (0, -1)
            case "R":
                vec = (0, 1)
            case _:
                raise ValueError(f"Unknown direction {direction}")

        for _ in range(length):
            head = head[0] + vec[0], head[1] + vec[1]
            prev = head
            for i, tail in enumerate(tails):
                match prev[0] - tail[0], prev[1] - tail[1]:
                    case (2, 0) | (-2, 0) | (0, 2) | (0, -2):
                        tails[i] = tail[0] + ((prev[0] - tail[0]) // 2), tail[1] + (
                            (prev[1] - tail[1]) // 2
                        )
                    case x, y if abs(x) > 1 or abs(y) > 1:
                        tails[i] = tail[0] + (1 if x > 0 else -1), tail[1] + (
                            1 if y > 0 else -1
                        )
                if i == 8:
                    visited.add(tails[i])

                prev = tails[i]

    print(f"Part 2: {len(visited)}")


if __name__ == "__main__":
    main()
