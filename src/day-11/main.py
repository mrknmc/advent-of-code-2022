import re
import dataclasses

monkey_re = r"^Monkey (\d+):"
starting_re = r"\s*Starting items: (.+)"
operation_re = r"\s*Operation: new = old ([+*]) (\d+|old)"
test_re = r"\s*Test: divisible by (\d+$)"
true_re = r"\s*If true: throw to monkey (\d+)"
false_re = r"\s*If false: throw to monkey (\d+)"


@dataclasses.dataclass
class Monkey:

    id_: int
    items: list[int]
    operator: str
    operand: int
    test: int
    test_true: int
    test_false: int
    count: int = 0


def main():
    lines = open("src/day-11/data1.txt", "r").read().split("\n\n")
    monkeys: list[Monkey] = []
    for block in lines:
        id_ = None
        items = None
        operator = None
        operand = None
        test = None
        test_true = None
        test_false = None
        for line in block.split("\n"):
            if match := re.match(monkey_re, line):
                id_ = int(match.groups()[0])
            elif match := re.match(starting_re, line):
                items = [int(item) for item in match.groups()[0].split(", ")]
            elif match := re.match(operation_re, line):
                operator = match.groups()[0]
                operand_str = str(match.groups()[1])
                operand = int(operand_str) if operand_str.isdecimal() else -1
            elif match := re.match(test_re, line):
                test = int(match.groups()[0])
            elif match := re.match(true_re, line):
                test_true = int(match.groups()[0])
            elif match := re.match(false_re, line):
                test_false = int(match.groups()[0])
        assert id_ is not None
        assert items is not None
        assert operator is not None
        assert operand is not None
        assert test is not None
        assert test_true is not None
        assert test_false is not None
        monkey = Monkey(
            id_=id_,
            items=items,
            operator=operator,
            operand=operand,
            test=test,
            test_true=test_true,
            test_false=test_false,
        )
        monkeys.append(monkey)

    monkey_clones = [
        Monkey(
            id_=m.id_,
            items=list(m.items),
            operator=m.operator,
            operand=m.operand,
            test=m.test,
            test_true=m.test_true,
            test_false=m.test_false
        )
        for m in monkeys
    ]

    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                func = item.__mul__ if monkey.operator == "*" else item.__add__
                num = item if monkey.operand == -1 else monkey.operand
                new_num = func(num)
                new_num = new_num // 3
                monkey.count = monkey.count + 1
                if new_num % monkey.test == 0:
                    monkeys[monkey.test_true].items.append(new_num)
                else:
                    monkeys[monkey.test_false].items.append(new_num)

    print(f"Part 1: {sorted(m.count for m in monkeys)[-2:]}")

    for i in range(10000):
        for monkey in monkey_clones:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                func = item.__mul__ if monkey.operator == "*" else item.__add__
                num = item if monkey.operand == -1 else monkey.operand
                new_num = func(num)
                monkey.count = monkey.count + 1
                if new_num % monkey.test == 0:
                    print(monkey.id_, 'true')
                    monkey_clones[monkey.test_true].items.append(new_num)
                else:
                    print(monkey.id_, 'false')
                    monkey_clones[monkey.test_false].items.append(new_num)

    print(f"Part 2: {sorted(m.count for m in monkey_clones)[-2:]}")


if __name__ == "__main__":
    main()
