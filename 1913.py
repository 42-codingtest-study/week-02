n = int(input())
find = int(input())
arr = [[0] * n for _ in range(n)]#초기화

x,y = n//2, n//2
num = 1 #1씩 증가하는 수
arr[x][y] = num
count = 0 #홀수인지 짝수인지
move_count = 1
coordinate_x = ''
coordinate_y = ''


while num != n*n:
    count += 1
    if count % 2 != 0:
        if move_count % 2 != 0:
            for i in range(move_count):
                x -= 1
                num += 1
                arr[x][y] = num
                if num == n*n:
                    break
        
        else:
            for i in range(move_count):
                x += 1
                num += 1
                arr[x][y] = num
                if num == n*n:
                    break
    else:
        if move_count % 2 != 0:
            for i in range(move_count):
                y += 1
                num += 1
                arr[x][y] = num
                if num == n*n:
                    break
            move_count += 1
        
        else:
            for i in range(move_count):
                y -= 1
                num += 1
                arr[x][y] = num
                if num == n*n:
                    break
            move_count += 1


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
        if arr[i][j] == find:
            coordinate_x  = i+1
            coordinate_y = j+1
    print()
print(coordinate_x, coordinate_y)
                
                