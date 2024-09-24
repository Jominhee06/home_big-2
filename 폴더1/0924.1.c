#include <stdio.h>

// 정수 n의 순차곱셉값을 반환
int factorial(int n)
{
	if (n > 0)
		return n * factorial(n - 1);
	else
		return 1;
}
int fact2(int num)
{
	int fact = 1;
	while (num > 0)
	{
		fact *= num--;
	}
	return fact;
}

int main(void) {
	int x;
	printf("Enter an integer:");
	scanf("%d", &x);
	printf("factorial(%d) = %d \n", x, factorial(x));

	return 0;
}