import sys

n = int(input())
s = set()

for i in range(n):
    #word = list(input().split())
    word = sys.stdin.readline().strip().split()

    if len(word) == 1:
        if word[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:   #empty
            s = set()
    else:
        command = word[0]
        target = int(word[1])

        if command == 'add':
            s.add(target)
        elif command == 'remove':
            s.discard(target)
        elif command == 'check':
            print(1 if target in s else 0)
        elif command == 'toggle':
            if target in s:
                s.discard(target)
            else:
                s.add(target)