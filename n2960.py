n, k = map(int, input().split())

num = list(range(2, n+1))
num.sort()
n = 0

while 1:
    p = num[0]

    for i in num:
        if i % p == 0:
            num.remove(i)
            n += 1
        if n == k:
            print(i)
            quit()