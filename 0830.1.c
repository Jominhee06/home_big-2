#include <stdio.h>

int main()
{
	int ary[5] = { 10,20,30,40,50 };
	int* pa = ary;
	int* pb = pa + 3;

	printf("pa : %u\n", pa);
	printf("pb : %u\n", pb);
	pa++;                               // pa�� ���� �迭 ��ҷ� �̵�
	printf("pb - pa : %u\n", pb - pa);  // �� �������� ����

	printf("�տ� �ִ� �迭 ����� �� ��� : ");

	if (pa < pb) printf("%d\n", *pa);      // pa�� �迭�� �տ� ������ *pa ���
	else printf("%d\n", *pb);              // pb�� �迭�� �տ� ������ *pb ���
	
	return 0;
}