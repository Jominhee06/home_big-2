#include <stdio.h>
//3번 swap 함수 호출

void swap(int* pa, int* pb);

int main(void) {

	int a = 20, b = 30;

	swap(&a, &b);
	printf("a:%d, b:%d\n", a, b);

	return 0;
}

void swap(int* pa, int* pb)   
{
	int temp;      

	temp = *pa;
	*pa = *pb;
	*pb = temp;
}