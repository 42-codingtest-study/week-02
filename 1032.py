# https://www.acmicpc.net/problem/1032

n = int(input())
lst = [input() for _ in range(n)]	# 받아준다
for i in range(len(lst[0])) :		# 각 문자열의 길이가 같으므로 첫번째 문자열의 길이를 쓴다
    flag = True						# false로 바뀌면 물음표 출력할것이다.
    same = lst[0][i]				# 이거랑 다른 문자가 나오면 false로 바뀜
    for j in lst :
        if (same != j[i]) :
            flag = False
    if (flag) :
        print(same, end = '')
    else :
        print("?", end = '')