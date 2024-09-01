#include <stdio.h>

int main() {
    int age = 25;          
    int chest = 95;         
    char size;              

    
    if (age == 25) {
        if (chest < 90) {
            size = 'S';
        }
        else if (chest <= 100) {
            size = 'M';
        }
        else {
            size = 'L';
        }
    }
    else {
        
        size = 'M';  
    }

    // 결과 출력
    printf("나이가 %d세이고 가슴둘레가 %d인 사람의 사이즈는 %c입니다.\n", age, chest, size);

    return 0;
}
