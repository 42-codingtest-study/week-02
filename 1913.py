# https://www.acmicpc.net/problem/1913

N = int(input())
M = int(input())
# 인덱스 계산을 N x N인 맵으로 하면 out of range 오류가 빈번히 일어날 가능성이 있기 때문에
lst = [[0] * (N) for _ in range(N)]		# 달팽이가 기어다닐 맵 생성
start = N // 2		# 처음 시작 위치
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
                answer = [x + 1, y + 1]
    if (x == 0 and y == 0) :
        break
    x -= 1
    y -= 1
    move += 2
for i in range(N) :
    print(*lst[i])
print(*answer)

## 위에거 안됨 .. 런타임에러 왜나지..

import  copy

n = int(input())
m = int(input())
snail = []
temp = []

for i in range(n):
    temp.append(0)

for i in range(n):
    snail.append(copy.deepcopy(temp))

move = [[0,1],[1,0],[0,-1],[-1,0]]
d = 0
now_x = 0 ; now_y = 0 ; now_num = n*n

while(now_num > 0):
    snail[now_y][now_x] = now_num
    if(now_x + move[d][0] < 0 or now_x + move[d][0] >= n or now_y + move[d][1] < 0 or now_y + move[d][1] >= n or snail[now_y+move[d][1]][now_x+move[d][0]] != 0):
        d = (d + 1) % 4
    now_y = now_y + move[d][1]
    now_x = now_x + move[d][0]
    now_num = now_num - 1

for i in range(n):
    for j in range(n):
        if(snail[i][j] == m):
            find_x = j
            find_y = i
        print(snail[i][j] , end = ' ')
    print()
print(find_y + 1,find_x + 1)