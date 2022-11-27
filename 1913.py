import sys

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())
num = n
snail = [[0] * n for _ in range(n)]

# 시작위치 찾기
x = (n - 1) // 2
y = (n - 1) // 2
snail[x][y] = 1

# 방향 [상, 하, 좌, 우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 칸 채우기
i = 2
start = 3

while x != 0 or y != 0:
	while i <= start * start:
		if (x == (n - 1) // 2) and (y == (n - 1) // 2):
			c_up, c_down, c_left, c_right = start, start - 1, start - 1, start - 2
			# 세팅 후, 한 칸 위로 올리기
			x += dx[0]
			y += dy[0]
			c_up -= 1

		elif c_right > 0: # 우
			x += dx[3]
			y += dy[3]
			c_right -= 1

		elif c_down > 0: # 하
			x += dx[1]
			y += dy[1]
			c_down -= 1

		elif c_left > 0: # 좌
			x += dx[2]
			y += dy[2]
			c_left -= 1

		elif c_up > 0: # 상
			x += dx[0]
			y += dy[0]
			c_up -= 1

		snail[x][y] = i
		i += 1

	#젤 안쪽 작은 원 그렸으면 그 다음 껍질 그리기
	n -= 2
	start += 2

# 출력하고, 위치 찾기
for i in snail:
	print(*i)
for i in range(num):
	for j in range(num):
		if snail[i][j] == target:
			print(i + 1, j + 1)
