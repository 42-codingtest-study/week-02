#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int	main()
{
	int	n, i;
	scanf("%d", &n);
	char	res[51], tmp[51];
	scanf("%s", res);
	n--;
	while(n--)
	{
		scanf("%s", tmp);
		i = 0;
		while (res[i])
		{
			if (res[i] != tmp[i])
				res[i] = '?';
			i++;
		}
	}
	printf ("%s", res);
}
