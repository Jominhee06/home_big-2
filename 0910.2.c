// bin_search 함수 이용

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
    int* x; // 배열에 첫번째 요소 주소

    puts("선형 검색");
    printf("요소 개수: ");
    scanf("%d", &nx);

    if (nx <= 0) {
        puts("Invalid number of elements.");
        return 1;
    }

    x = calloc(nx, sizeof(int)); // 요소의 개수가 nx인 int형 배열 x를 생성
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

    idx = bin_search(x, nx, ky); // 배열 x에서 값이 ky인 요소를 이진 검색
    if (idx == -1)
        puts("Search Failed");
    else
        printf("%d is in the x[%d].\n", ky, idx);

    free(x);
    return 0;
}