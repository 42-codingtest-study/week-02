import sys
from itertools import permutations

n = int(input())
# 순열(123,124,125 ... 등 조합 찾아줌)
posb = list(permutations('123456789', 3))

for _ in range(n):
	minh, strk, ball = map(int, sys.stdin.readline().split())
	minh = list(str(minh))
	rmcnt = 0
	for i in range(len(posb)):
		s, b = 0, 0
		# 제대로 위치를 찾기위해(0부터 시작)
		i -= rmcnt
		for j in range(3):
			if posb[i][j] == minh[j]:
				s += 1
			elif minh[j] in posb[i]:
				b += 1
		#검증
		if strk != s or ball != b:
			posb.remove(posb[i])
			rmcnt += 1

print(len(posb))