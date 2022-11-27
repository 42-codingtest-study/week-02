n = int(input())

for i in range(n):
    new = list(input())

    if i == 0:
        result = new
    else:
        for j in range(len(result)):
            for k in range(len(new)):
                if j == k:
                    if result[j] != new[k]:
                        result[j] = '?'

for l in result:
    print(l, end='')