# https://www.acmicpc.net/problem/2960

N, K = map(int, input().split())
eratos = set([i for i in range(2, N + 1)])
while (len(eratos) > 0) :
    eratos_min = min(eratos)		# 기준 1
    eratos_max = max(eratos)		# 기준 2
    tmp = min(eratos)				# 배수
    i = 1
    while (tmp <= eratos_max) :
        if (tmp in eratos) :		# set 안에 값 있으면 제거
            eratos.remove(tmp)
            K -= 1
            if (K == 0) :
                print(tmp)
        i += 1
        tmp = eratos_min * i
    if (K == 0) :
        break
