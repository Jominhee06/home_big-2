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

    // ��� ���
    printf("���̰� %d���̰� �����ѷ��� %d�� ����� ������� %c�Դϴ�.\n", age, chest, size);

    return 0;
}
