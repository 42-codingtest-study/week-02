# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline
S = set()   #list 쓰면 시간 초과
T = int(input())
for i in range(T):
    tmp = input().split()
    if len(tmp) == 1:
        if tmp[0] == 'all':
            S = set([x for x in range(1, 21)])
        else:
            S = set()

    else:
        cmd, x = tmp[0], int(tmp[1])
        if cmd == 'add':
            S.add(x)
        elif cmd == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif cmd == 'remove':
            if x in S:
                S.discard(x)    #요소 삭제
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)