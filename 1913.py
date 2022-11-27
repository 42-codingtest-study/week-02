n, m = int(input()), int(input())

# 달팽이 모양이 될 표 생성 🐌🐌🐌🐌🐌🐌🐌
table = [0 for _ in range(n * n)]

# 각각 up, right, down, left를 의미
direction = [-n, 1, n, -1]

# 초기값 세팅
idx = (n * n - 1) // 2
table[idx] = 1
level = 3
num = 2

# 방향에 따라 인덱스를 바꾸고 표를 채우는 함수
def putTable(dir):
    # global: 함수 안에서 전역 변수의 값을 변경하고 싶을 때 사용하는 키워드
    global idx, num
    idx += direction[dir]
    table[idx] = num
    num += 1

# 표가 모두 채워질 때까지 반복 🐌🐌🐌🐌
while 0 in table:
    while num <= level * level:
        # 시작점이면 한 칸 위로
        putTable(0)

        # n - 2번 오른쪽으로 이동
        for _ in range(level - 2):
            putTable(1)

        # n - 1번 아래쪽으로 이동
        for _ in range(level - 1):
            putTable(2)

        # n - 1번 왼쪽으로 이동
        for _ in range(level - 1):
            putTable(3)

        # n - 1번 위쪽으로 이동
        for _ in range(level - 1):
            putTable(0)
    
    # 3, 5, 7, ...
    level += 2

# 결과 출력
for i in range(n):
    for j in range(n):
        print(table[i * n + j], end=' ')
        if table[i * n + j] == m:
            x, y = i + 1, j + 1
    print()
print(x, y)