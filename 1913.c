#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void	printboard(int n, int board[][n], int target)
{
	int	y = -1, x, target_x, target_y;

	while (++y < n)
	{
		x = -1;
		while (++x < n)
		{
			printf("%d ", board[y][x]);
			if (board[y][x] == target)
			{
				target_x = x + 1;
				target_y = y + 1;
			}
		}
		printf("\n");
	}
	printf("%d %d\n", target_y, target_x);
}


int	main()
{
	int	n, y = 0,x = 0,num, target, signal = 1, repeat = 0;//repeat == 몇바퀴 돌았는지

	scanf("%d %d", &n, &target);
	int	board[n][n];
	num = n * n + 1;// n* n 넣어서 0되기 전까지 반복
	while (--num)
	{
		board[y][x] = num;
		if ((signal == 1 && y == n - 1 - repeat)// 왼쪽아래 끝
		|| (signal == 2 && x == n - 1 - repeat)// 오른쪽 아래 끝
		|| (signal == 3 && y == repeat))// 오른쪽 위
			signal++;
		else if (signal == 4 && x == repeat + 1)// 왼쪽 위 + 1
		{
			repeat++;
			signal = 1;
		}
		if (signal == 1)
			y++;
		else if (signal == 2)
			x++;
		else if (signal == 3)
			y--;
		else if (signal == 4)
			x--;
	}
	printboard(n, board, target);
}
