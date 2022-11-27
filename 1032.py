num = int(input())
target1 = list(str(input()))

for i in range (0, num - 1):
	target2 = list(str(input()))
	for j in range (len(target2)):
		if target1[j] != target2[j]:
			target1[j] = '?'

print(''.join(target1))