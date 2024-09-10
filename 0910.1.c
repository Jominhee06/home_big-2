#include <stdio.h>
#include <stdlib.h>

int search(int a[], int n, int key) {
    int i = 0;
    a[n] = key; // Place the sentinel value at the end of the array

    while (a[i] != key) {
        i++;
    }

    return i == n ? -1 : i; // Return -1 if key was not found, otherwise return index
}

int main(void) {
    int i, nx, ky, idx;
    int* x; // Pointer to the first element of the array

    puts("선형 검색");
    printf("요소 개수: ");
    scanf("%d", &nx);

    if (nx <= 0) {
        puts("Invalid number of elements.");
        return 1;
    }

    x = calloc(nx + 1, sizeof(int)); // Allocate space for nx elements + 1 sentinel
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

    idx = search(x, nx, ky); // Perform the linear search
    if (idx == -1)
        puts("Search Failed");
    else
        printf("%d is in x[%d].\n", ky, idx);

    free(x); // Free the allocated memory
    return 0;
}
