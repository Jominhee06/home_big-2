#include <stdio.h>
//1�� �����
int main(void)
{
	for (int i = 0; i < 3; i++)
	{
		for (int k = 0; k > 3-k-1; k--)
		{
			printf(" ");
		}
		for (int j = 0; j < (2 * i) + 1; j++) 
		{
			printf("*");
		}
		
		printf("\n");
	}
	return 0;
}