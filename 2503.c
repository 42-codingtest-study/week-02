#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int strtest(char test[], int str, char a, char b, char c)
{
	int cnt = 0;

	if (test[0] == a)
		cnt++;
	if (test[1] == b)
		cnt++;
	if (test[2] == c)
		cnt++;
	if (str == cnt)
		return (1);
	return (0);
}

int	balltest(char test[], int ball, char a, char b, char c)
{
	int	cnt = 0;

	if (test[1] == a || test[2] == a)
		cnt++;
	if (test[0] == b || test[2] == b)
		cnt++;
	if (test[0] == c || test[1] == c)
		cnt++;
	if (ball == cnt)
		return (1);
	return (0);
}

int	ft_test(char test[], int str, int ball, char a, char b, char c)
{
	if (strtest(test, str, a, b, c) == 0)
		return (0);
	if (balltest(test, ball, a, b, c) == 0)
		return (0);
	return (1);
}



int	main()
{
	int	n, i = -1, cnt = 0;
	char	a = '0', b, c;

	scanf("%d", &n);
	char	test[n + 1][4], str[n + 1][2], ball[n + 1][2]; //test == 숫자 str == 스트라이크 ball == 볼

	while (++i < n)
		scanf("%s %s %s", test[i], str[i], ball[i]);

	while (++a <= '9')
	{
		b = '0';
		while (++b <= '9')
		{
			c = '0';
			while (++c <= '9')
			{
				if (a == b || b == c || a == c) // 숫자 같은거빼주기 ex) 111, 122
					;
				else
				{
					i = -1;
					while (++i < n)
					{
						if (ft_test(test[i], str[i][0] - '0', ball[i][0] - '0', a, b, c) == 0)
							break ;
					}
					if (i == n)
						cnt++;
				}
			}
		}
	}
	printf("%d", cnt);
}

//성불 완료
