// bin_search �Լ� �̿�

#include <stdio.h>
#include <stdlib.h>

int bin_search(const int a[], int n, int key) 
{
    int pl = 0;
    int pr = n - 1;
    int pc;

    do {
        pc = (pr + pl) / 2;
        if (a[pc] == key) return pc;
        else if (a[pc] < key)
            pl = pc + 1;
        else
            pr = pc - 1;
    } while (pl <= pr);
    return -1;
}

int main(void) {
    int i, nx, ky, idx;
    int* x; // �迭�� ù��° ��� �ּ�

    puts("���� �˻�");
    printf("��� ����: ");
    scanf("%d", &nx);

    if (nx <= 0) {
        puts("Invalid number of elements.");
        return 1;
    }

    x = calloc(nx, sizeof(int)); // ����� ������ nx�� int�� �迭 x�� ����
    if (x == NULL) {
        puts("Memory allocation failed.");
        return 1;
    }

    for (i = 0; i < nx; i++) {
        printf("x[%d]: ", i);
        scanf("%d", &x[i]);
    }

    printf("Search Num: ");
    scanf("%d", &ky);

    idx = bin_search(x, nx, ky); // �迭 x���� ���� ky�� ��Ҹ� ���� �˻�
    if (idx == -1)
        puts("Search Failed");
    else
        printf("%d is in the x[%d].\n", ky, idx);

    free(x);
    return 0;
}