#include <stdio.h>

void print_ary(int* pa, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", pa[i]); 
    }
    printf("\n");  
}

int main() {
    
    int ary1[] = { 10, 20, 30, 40, 50 };
    int ary2[] = { 10, 20, 30, 40, 50, 60, 70 };
    int size1 = sizeof(ary1) / sizeof(ary1[0]);
    int size2 = sizeof(ary2) / sizeof(ary2[0]);

    printf("ary1 배열의 요소들: ");
    print_ary(ary1, size1);

    printf("ary2 배열의 요소들: ");
    print_ary(ary2, size2);

    return 0;
}
