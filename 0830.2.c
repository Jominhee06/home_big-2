#include <stdio.h>
#include <string.h>
#include <stdlib.h> // # -> ��ó����

int main()
{
	char s1[11] = "23@45@67#50";  // s1 = ���� �ּ� ����
	char* ptr = strtok(s1, "@#");  // strtok = ���ڿ��� �и����ִ� ���� �Լ�
	int num[5];    // �迭������ ����ȯ�� �����͸� ����
	int str = 0;   // �迭 �ε����� �����ϱ� ���� ���� ���� ����

	while (ptr != NULL) // ptr�� ���� �ƴѰ�� �ݺ��ؼ� �����Ѵ�.
	{
		num[str] = atoi(ptr); // atoi = ���� ��Ʈ���� ���������� ��ȯ�ϴ� �Լ�, ptr�� �ɰ��� ù��° ���ڿ��� ������ �ִ�.
		//printf("%s\n", ptr);
		printf("%d\n", num[str]); // num�� ������ str�� �����͸� ���
		str++; // str�� ������ ����
		ptr = strtok(NULL, "@#");  // NULL = �����ּ�
	}
	return 0; // ��ȯ�ϴ� �Լ�
}

// static = �ϳ��� �������Ϸ� ����