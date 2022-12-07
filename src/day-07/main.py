from collections import defaultdict
import dataclasses
import re

from typing import Optional

FILE_RE = r'^(\d+) (.+)$'
DIR_RE = r'^dir (.+)$'
CMD_CD_RE = r'^\$ cd (.+)$'
CMD_LS_RE = r'^\$ ls$'


@dataclasses.dataclass
class Node:

    name: str
    children: list['Node']
    size: int
    parent: Optional['Node']


def main():
    lines = [l.strip() for l in open('src/day-07/data1.txt', 'r').readlines()]

    root_dir = Node(name='/', children=[], size=0, parent=None)
    cur_dir = root_dir

    for line in lines:
        if match := re.match(CMD_CD_RE, line):
            dir_name = match.groups()[0]
            if dir_name == '/':
                cur_dir = root_dir
            elif dir_name == '..':
                assert cur_dir.parent, 'current dir has no parent!'
                cur_dir = cur_dir.parent
            else:
                cur_dir = next(f for f in cur_dir.children if f.name == dir_name)
        elif match := re.match(CMD_LS_RE, line):
            pass
        elif match := re.match(DIR_RE, line):
            node = Node(name=match.groups()[0], children=[], size=0, parent=cur_dir)
            cur_dir.children.append(node)
        elif match := re.match(FILE_RE, line):
            node = Node(name=match.groups()[1], children=[], size=int(match.groups()[0]), parent=cur_dir)
            cur_dir.children.append(node)
        else:
            raise NotImplementedError(line)

    # calculate dir sizes
    files = [root_dir]
    visited = set()
    while len(files) > 0:
        file = files.pop()
        if len(file.children) > 0 and id(file) not in visited:
            files.append(file)
            files.extend(file.children)
        if file.parent is not None:
            file.parent.size += file.size
        visited.add(id(file))

    total_size = 0
    files = [root_dir]
    while len(files) > 0:
        file = files.pop(0)
        files.extend(file.children)
        if len(file.children) > 0 and file.size <= 100000:
            total_size += file.size

    print(f'Part 1: {total_size}')

    available = 70000000 - root_dir.size
    needed = 30000000
    missing = needed - available

    min_size = root_dir.size

    files = [root_dir]
    while len(files) > 0:
        file = files.pop(0)
        files.extend(file.children)
        if len(file.children) > 0 and file.size >= missing and file.size <= min_size:
            min_size = file.size

    print(f'Part 2: {min_size}')


if __name__ == '__main__':
    main()