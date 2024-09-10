#include <stdio.h>
#include <stdlib.h>

int search(const int a[], int n, int key) {
    int i = 0;
    while (1) {
        if (i == n) return -1;
        if (a[i] == key) return i;
        i++;
    }
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

    x == calloc(nx, sizeof(int)); //����� ������ nx
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

    idx = search(x, nx, ky); // �迭�� �ּ�:x
    if (idx == -1)
        puts("Search Failed");
    else
        printf("%d is in the x[%d].\n", ky, idx);

    free(x);
    return 0;
}
