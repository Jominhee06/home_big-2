#include <stdio.h>
//1¹ø º°Âï±â
int main(void)
{
	for (int i = 0; i < 3; i++)
	{
		for (int k = 5; k > 1+ ( 2 * i); k--)
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