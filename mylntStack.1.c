#include <stdio.h>
#include "mylntStack.h"

int main()
{
	IntStack s;
	if (Initialize(&s, 64) == -1)
	{
		puts("���� ������ �����߽��ϴ�.");
		return -1;
	}

	while (1)
	{
		int meun, x;
		printf("���� ������ ��: %d / %d\n", Size(&s), Capacity(&s));
		printf("(1)Ǫ�� (2)�� (3)��ũ (4)��� (0)����: ");
		scanf("%d", &meun);

		if (meun == 0) break;
		
		switch (meun)
		{
		case 1:
			printf("data: ");
			scanf("%d", &x);
			if (Push(&s, x) == -1)
				puts("\a����: Ǫ�ÿ� �����߽��ϴ�.");
			break;

		case 2:
			if (Pop(&s, &x) == -1)
				puts("\a����: �˿� �����߽��ϴ�.");
			else
				printf("�� �����ʹ� %d�Դϴ�. \n", x);
			break;

		case 3:
			if (Peek(&s, &x) == -1)
				puts("\a����: ��ũ�� �����߽��ϴ�.");
			else
				printf("��ũ �����ʹ� &d�Դϴ�. \n", x);
			break;

		case 4:
			Print(&s);
			break;
		}
	}
	Terminate(&s);
	return 0;
}