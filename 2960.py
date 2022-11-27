n, target = map(int, input().split())
n_list = [True] * (n+1)
cnt = 0

for i in range(2, n + 1):
	if n_list[i] == True:
		#배수니까 i만큼씩 커지면 됨.
		for j in range(i, n + 1, i):
			if n_list[j] == True:
				n_list[j] = False
				cnt += 1
				if cnt == target:
					print(j)
					exit()