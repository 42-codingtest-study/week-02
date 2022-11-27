# https://www.acmicpc.net/problem/2503

N = int(input())
score_lst = [list(str(i)) for i in range(123, 1000) if (len(set(list(str(i)))) == 3 and '0' not in set(list(str(i))))]
print(score_lst)
for _ in range(N) :
    n, s, b = map(int, input().split())
    n = list(str(n))  # int는 리스트가 될 수 없다
    removeCount = 0
    for i in range(len(score_lst)):
        strike = ball = 0
        i -= removeCount  # num[0]부터 조회해야함
        for j in range(3):
            if score_lst[i][j] == n[j]: # 입력한 숫자(한자리)와 num의 숫자(한자리)가 같으면 strike ++
                strike += 1
            elif n[j] in score_lst[i]:  # 입력한 숫자(한자리)가 num안에 들어있으면 ball ++
                ball += 1

        if (strike != s) or (ball != b): # 입력받은 s,b와 다르면 num에서 삭제
            score_lst.remove(score_lst[i])
            removeCount += 1

print(len(score_lst))
