# 입력값 받기
n = int(input())
files = []
for _ in range(n):
    files.append(input())

result = ""
# 파일 이름의 길이만큼 반복문을 돌면서 비교
for i in range(len(files[0])):
    flag = 1
    for j in range(n - 1):
        # 값이 다르면 flag 0으로 바꾸고 break
        if files[j][i] != files[j + 1][i]:
            flag = 0
            break
    if flag:
        result += files[0][i]
    else:
        result += '?'

print(result)