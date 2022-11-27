# 입력값 받기
n, k = map(int, input().split())

# 모두 1로 초기화
arr = [1 for _ in range (n + 1)]

# 에라토스테네스의 체
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if arr[j] == 1:
            arr[j] = 0
            # k번째 수를 찾기 위해 줄여나감
            k -= 1
            if k == 0:
                print(j)
                break