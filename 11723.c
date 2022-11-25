#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int	is_up_nine(char *s, int index)
{
	if (s[index])//두번째 자리수가 널이아니면
		return (1);
	return (0);
}

int	checker(char *s, char *retarr)
{
	int	i = 0;
	char *add = "add ";
	char *remove = "remove ";
	char *check = "check ";
	char *toggle = "toggle ";
	char *all = "all";
	char *empty = "empty";

	if (strncmp(add, s, 4) == 0)// 명령 부분이 똑같으면
	{
		i = 0;
		while (retarr[i])
			i++;
		if (is_up_nine(s, 6))
			retarr[i] = s[5] * 10 + s[6];
		else
			retarr[i] = s[5];
	}
}




int	main()
{
	int	n, i = -1;

	scanf("%d", &n);
	char	retarr[n + 1];

	while (++i < n)
		retarr[i] = 0;//모든 어레이에 널 넣어주기


}
