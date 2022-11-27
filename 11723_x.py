num = int(input())
s = [0] * 20

for i in range (num):
	# input()함수는 sys.stdin.readline()과 비교해서  
	# prompt message를 출력하고, 
	# 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
	command = list(map(str, input().split()))
	# command = sys.stdin.readline().strip().split()
	# 로 해주면 통과
	op = command[0] 
	if not (op == 'all' or op == 'empty'):
		target = int(command[1]) - 1
	if op == 'add':
		s[target] = 1
	elif op == 'remove':
		s[target] = 0
	elif op == 'check':
		print(s[target])
	elif op == 'toggle':
		if s[target] == 1:
			s[target] = 0
		else:
			s[target] = 1
	elif op == 'all':
		s = [1] * 20
	elif op == 'empty':
		s = [0] * 20