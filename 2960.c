#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int	main()
{
	int	n, k, i, p;

	scanf("%d %d", &n, &k);

	int	arr[n * 2];
	i = 1;
	while (++i <= n * 2)// 다 1로 넣어줌
		arr[i] = 1;
	i = 2;
	while (1)
	{
		i = 2;
		while (arr[i] == 0)// 제일 작은 소수 찾기
			i++;
		p = i;
		while (p <= n)
		{
			if (k > 1)
			{
				arr[p] = 0;
				k--;
			}
			else//찾았다
			{
				printf("%d", p);
				return (0);
			}
			while (arr[p] == 0)//이미 지운 수면 넘기기
				p += i;
		}
	}
}
