from itertools import permutations


''' 순열 안쓰고 사용
n = int(input())
number = list(range(123, 988))

#영수 숫자 후보
for i in number:
    i = str(i)
    if '0' in i:
        number.remove(int(i))
    elif i[0] == i[1] or i[1] == i[2] or i[2] == i[0]:
        number.remove(int(i))

#민혁이 질문 답
for i in range(n):
    num, s, b = map(int, input().split())
    num = str(num)

    if s == 3:
        quit()
    elif s == 2:

    if b == 3:
        for j in number:
            j = str(j)
            if num[0] not in j:
                number.remove(int(j))
            elif num[1] not in j:
                number.remove(int(j))
            elif num[2] not in j:
                number.remove(int(j))

'''
n = int(input())
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # 리스트에 숫자를 미리 넣기

for _ in range(n):
    q, strk, ball = map(int, input().split())
    removed = 0  # 중간의 리스트 길이를 변경하기 때문에 필요한 변수
    q = list(str(q))

    for i in range(len(num)):
        sCnt, bCnt = 0, 0
        i -= removed
        for j in range(3):
            q[j] = int(q[j])
            if q[j] in num[i]:  # 질문한 숫자의 j번 인덱스의 숫자가 num의 i번째 튜플에 있는가
                if j == num[i].index(q[j]):  # 있고, 위치도 같으면 스트라이크 횟수 ++
                    sCnt += 1
                else:  # 위치는 다르지만 있다면 볼 횟수 ++
                    bCnt += 1
        if sCnt != strk or bCnt != ball:  # 질문을 통해 얻은 답변과, 순열을 통해 얻은 스트라이크, 볼 횟수가 다르면
            num.remove(num[i])  # 후보지에서 제외
            removed += 1  # 달라진 리스트 길이를 이해 removed --
print(len(num)) # 다 지우고 남은 선택지 갯수