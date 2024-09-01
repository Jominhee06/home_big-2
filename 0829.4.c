#include <stdio.h>


double find_max(double* pa, int size) {
    double max = pa[0]; 

    for (int i = 1; i < size; i++) {
        if (pa[i] > max) {
            max = pa[i];  
        }
    }

    return max;
}

int main() {
   
    double ary[] = { 2.5, 3.1, 5.5, 7.1, 4.6, 9.9, 1.5 };
    int size = sizeof(ary) / sizeof(ary[0]);
    double max = find_max(ary, size);

    printf("배열의 최대값 : %.2f\n", max);

    return 0;
}
