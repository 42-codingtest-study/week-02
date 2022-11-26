import sys

# 시간 초과 이슈 ...
# input() -> sys.stdin.readlint()
# set -> list

n = int(sys.stdin.readline())
s = [0 for i in range(21)]

for _ in range(n):
    # command, x 초기화
    line = sys.stdin.readline().split()
    if len(line) == 1:
        command = line[0]
    else:
        command, x = line[0], int(line[1])

    # command에 따라 처리
    if command == "add":
        s[x] = 1
    elif command == "remove":
        s[x] = 0
    elif command == "check":
        if s[x] == 1: print(1)
        else: print(0)
    elif command == "toggle":
        if s[x] == 1: s[x] = 0
        else: s[x] = 1
    elif command == "all":
        s = [1 for i in range(21)]
    elif command == "empty":
        s = [0 for i in range(21)]