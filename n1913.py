# 다시

n = int(input())
target = int(input())

# 상, 우, 하, 좌
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# 처음 1 위치 x, y에 넣어줌
if n % 2 == 1:
    x, y = n//2, n//2
else:
    x, y = n//2, n//2 - 1

m = [[0] * n for _ in range(n)]
m[x][y] = 1
cnt = 2
dir = 0
num = 2
while True:
    for _ in range(cnt-1):
        nx, ny = x + dx[dir], y + dy[dir]
        m[nx][ny] = num
        num += 1

        if num == n**2+1:
            break
        x, y = nx, ny

    if num == n**2+1:
        break

    dir = (dir + 1) % 4
    # 위나 아래로 갈때 숫자 1 증가
    if dir == 0 or dir == 2:
        cnt += 1

for i in m:
    print(*i)
for i in range(n):
    for j in range(n):
        if m[i][j] == target:
            print(i + 1, j + 1)