# https://www.acmicpc.net/problem/1913

N = int(input())
M = int(input())
# 인덱스 계산을 N x N인 맵으로 하면 out of range 오류가 빈번히 일어날 가능성이 있기 때문에
lst = [[0] * (N + 2) for _ in range(N + 2)]		# 달팽이가 기어다닐 맵 생성
start = N // 2 + 1		# 처음 시작 위치
lst[start][start] = 1
x = start
y = start
snail = 1
move = 0
dr = [0, 1, 0, -1] # 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
dc = [1, 0, -1, 0]
while (move <= N) :
    for i in range(4):
        for _ in range(move):  # 특정 방향으로 한칸씩 이동하며 숫자 입력
            x += dr[i]
            y += dc[i]
            snail += 1
            lst[x][y] = snail
            if snail == M:  # 찾을 번호의 인덱스 저장
                answer = [x, y]
    x -= 1
    y -= 1
    move += 2
for i in range(1, N + 1) :
    print(' '.join([str(lst[i][j]) for j in range(1, N + 1)]))
print(' '.join([str(i) for i in answer]))