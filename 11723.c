#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int	checker(char *signal, int *set)
{
	int	i = 0, num;
	char *add = "add";
	char *remove = "remove";
	char *check = "check";
	char *toggle = "toggle";
	char *all = "all";
	char *empty = "empty";

	scanf("%d", &num);
	if (strcmp(add, signal) == 0)// 명령 부분이 똑같으면
	{
		set[num]++;
		return (-1);
	}
	else if (strcmp(remove, signal) == 0)
	{
		set[num] = 0;
		return (-1);
	}
	else if (strcmp(check, signal) == 0)
	{
		if (set[num] == 0)
			return (0);
		else
			return (1);
	}
	else if (strcmp(toggle, signal) == 0)
	{
		if (set[num] == 0)
			set[num] = 1;
		else
			set[num] = 0;
		return (-1);
	}
	else if (strcmp(all, signal) == 0)
	{
		i = 0;
		while (++i < 21)
			set[i] = 1;
		return (-1);
	}
	else if (strcmp(empty, signal) == 0)
	{
		i = 0;
		while (++i < 21)
			set[i] = 0;
		return (-1);
	}
}

int	main()
{
	int	n, i = -1, check;
	int	set[21] = { 0 };
	char signal[10];
	scanf("%d", &n);

	while (++i < n)
	{
		scanf("%s", signal);
		check = checker(signal, set);
		if (check == 1)
			printf("1\n");
		else if (check == 0)
			printf("0\n");
	}
}
