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

// �� �Լ� (bsearch���� ���)
int int_cmp(const void* a, const void* b) {
    int int_a = *(const int*)a;
    int int_b = *(const int*)b;
    return (int_a > int_b) - (int_a < int_b);
}

int main(void) {
    int i, nx, ky;
    int* x; // �迭�� ù��° ��� �ּ�

    puts("Doing bsearch()");
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

    // �迭�� �����մϴ�. bsearch�� ����ϱ� ���� �迭�� ���ĵǾ� �־�� �մϴ�.
    qsort(x, nx, sizeof(int), int_cmp);

    printf("Search Num: ");
    scanf("%d", &ky);

    // bsearch�� ����Ͽ� �迭 x���� ���� ky�� ��Ҹ� �˻��մϴ�.
    int* p = bsearch(&ky, x, nx, sizeof(int), int_cmp);

    if (p == NULL)
        puts("Search Failed");
    else
        printf("%d is in x[%d].\n", ky, (int)(p - x)); // �ε��� ���

    free(x); // �迭 x�� ����
    return 0;
}
