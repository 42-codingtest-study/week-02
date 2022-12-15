import sys
input = sys.stdin.readline

n = int(input())
res = set()
for i in range(n):
    cmd = input().split()
    if cmd[0] == "add":
        res.add(int(cmd[1]))
 
    elif cmd[0] == "remove":
        if int(cmd[1]) in res:
            res.remove(int(cmd[1]))

    elif cmd[0] == "check":
        if int(cmd[1]) in res:
            print(1)
        else :
            print(0)

    elif cmd[0] == "toggle":
        if int(cmd[1]) in res:
            res.remove(int(cmd[1]))
        else:
            res.add(int(cmd[1]))    

    elif cmd[0] == "all":
        res = set([i for i in range(1, 21)])
  
    elif cmd[0] == "empty":
        res.clear() #clear 리스트 내의 모든 원소 삭제


    
        