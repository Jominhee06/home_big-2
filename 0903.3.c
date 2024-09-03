// 1.������ �������� ������ Ƚ�� �ڵ�

#include <stdio.h>

int main()
{
	int i, n;
	int prime[500];
	int ptr = 0;   // ������ �Ҽ��� ����� ��ġ ptr+1 --> �Ҽ�����
	unsigned long counter = 0;  // ���� Ƚ��
	prime[ptr++] = 2; // �ʱ� �Ҽ� 2
	prime[ptr++] = 3;

	for (n = 5; n < 1000; n += 2) {   // n�� 5���� ���� ��Ű�鼭 �ڱ⺸�� ���� �Ҽ��� ������
		int flag = 0;
		for (i = 1; counter++, prime[i] * prime[i] <= n; i++) {
			counter++;
			if (n % prime[i] == 0){
				flag = 1;
				break;
			}
		}
		if (! flag)
			prime[ptr++] = n;

		//if (ptr == i) prime[ptr++] = n;  // ������ �Ҽ�(ptr)���� �ߴµ� ������ ���ݼ��� �Ҽ� 
	}
	for (i = 0; i < ptr; i++) 
		printf("%d\n", prime[i]); 
	printf("������ �������� ������ Ƚ�� : %lu\n", counter);

	return 0;
}


// 2. �������� ������ Ƚ�� �ڵ�

//#include <stdio.h>
//
//int main(void) {
//	int i, n;
//	int prime[500];
//	int ptr = 0; // ptr�� �Ҽ��� ���� ����(x+1��° �Ҽ�)
//
//	unsigned long counter = 0;
//	prime[ptr++] = 2;
//
//	//---------- n�� 3���� ���� ��Ű�鼭 �ڱ⺸�� ���� �Ҽ��� ������ 
//	for (n = 3; n <= 1000; n += 2) {
//		for (i = 0; i < ptr; i++) {
//			counter++;
//			if (n % prime[i] == 0) break;
//		}
//
//		if (ptr == i) prime[ptr++] = n; //������ �Ҽ�(ptr)���� �ߴµ� ������ ���ݼ��� �Ҽ�
//	}
//
//	for (i = 0; i < ptr; i++) printf("%d\n", prime[i]);
//
//	printf("�������������� Ƚ��: %ul\n", counter);
//
//	return 0;
//}