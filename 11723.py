# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

# https://www.acmicpc.net/problem/11723

S = []
for _ in range(int(input())) :
    lst = list(input().split())
    if (lst[0] == 'add') :
        S.append(lst[1])
    elif (lst[0] == 'remove') :
        S.remove(lst[1])
    elif (lst[0] == 'check') :
        if (lst[1] in S) :
            print(1)
        else :
            print(0)
    elif (lst[0] == 'toggle') :
        if (lst[1] in S) :
            S.remove(lst[1])
        else :
            S.append(lst[1])
    elif (lst[0] == 'all') :
        S = [str(i) for i in range(1, 21)]
    elif (lst[0] == 'empty') :
        S = []
