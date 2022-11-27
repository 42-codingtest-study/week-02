import sys

num = int(input())
s = [0] * 20

for i in range (num):
	command = sys.stdin.readline().strip().split()

	if len(command) == 1:
		if command[0] == 'all':
			s = [1] * 20
		else:
			s = [0] * 20
	else:
		op, target = command[0], int(command[1]) - 1
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