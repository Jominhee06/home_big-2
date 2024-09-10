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

// 비교 함수 (bsearch에서 사용)
int int_cmp(const void* a, const void* b) {
    int int_a = *(const int*)a;
    int int_b = *(const int*)b;
    return (int_a > int_b) - (int_a < int_b);
}

int main(void) {
    int i, nx, ky;
    int* x; // 배열에 첫번째 요소 주소

    puts("Doing bsearch()");
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

    // 배열을 정렬합니다. bsearch를 사용하기 전에 배열이 정렬되어 있어야 합니다.
    qsort(x, nx, sizeof(int), int_cmp);

    printf("Search Num: ");
    scanf("%d", &ky);

    // bsearch를 사용하여 배열 x에서 값이 ky인 요소를 검색합니다.
    int* p = bsearch(&ky, x, nx, sizeof(int), int_cmp);

    if (p == NULL)
        puts("Search Failed");
    else
        printf("%d is in x[%d].\n", ky, (int)(p - x)); // 인덱스 계산

    free(x); // 배열 x를 해제
    return 0;
}
