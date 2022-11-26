import itertools

ztn = list(i for i in range (1, 10)) #가능한 숫자들을 리스트에 담아줌 1~9
target = list(itertools.permutations(ztn,3)) #숫자 3개씩 중복없이 담아주는 역할 파이썬조타,,,

n = int(input())
for _ in range(n):
    three, s, b = map(int, input().split())
    three = list(str(three))
    idx = 0
    
    for i in range(len(target)):
        strike = 0
        ball = 0
        i -= idx
        
        for j in range(3):
            three[j] = int(three[j])
            if three[j] == target[i][j]:
                strike += 1
            elif three[j]in target[i]:
                ball += 1
                
        if strike != s or ball != b:
            target.remove(target[i])
            idx+=1
            
print(len(target))    