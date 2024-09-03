// 정수를 2진수 ~ 36진수로 기수 변환
#include <stdio.h>
#define swap(type, x,y) do{type t = x; x=y; y=t;}while(0)  // 역순으로 바꾸는 선언문

// 정수 값 x를 n진수로 변환하여 배열 d에 아랫자리부터 저장
int card_convr(unsigned x, int n, char d[])
{
	char dchar[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	int digits = 0;  // 변환 후 자릿수

	if (x == 0)  // 0이면
		d[digits++] = dchar[0];  // 변환 후에도 0
	else
		while(x){   // 몫이 0이 될때까지, 마지막수는 몫이 0 나머지가 마지막 몫
			d[digits++] = dchar[x % n];   // n으로 나눈 나머지를 저장
			x /= n;  // x = x /n (정수 몫)
		}
	for (int i = 0; i < digits / 2; i++) swap(char, d[i], d[digits - 1 - i]);   // 역순으로 바꾸는 반복문

	return digits;
}



int main(void)
{
	int i;         
	unsigned no;   // 변환하는 정수
	int cd;        // 기수(진법수)
	int dno;       // 변환 후 자릿수
	char cno[512]; // 변환한 값의 각 자리의 숫자를 저장하는 문자 배열
	int retry;     // 한번더

	puts("10진수를 기수 변환합니다.");
	do {
		printf("변환하는 음이 아닌 정수 : ");
		scanf("%u", &no);

		do {
			printf("어떤 진수로 변환할까요? (2-36) : ");
			scanf("%d", &cd);
		} while (cd < 2 || cd > 36);

		dno = card_convr(no, cd, cno);    // no를 cd진수로 변환

		printf("%d진수로는", cd);
		for (i = dno - 1; i >= 0; i--)   // 윗자리부터 차례로 출력
			printf("%c", cno[i]);
		printf("입니다.\n");

		printf("한 번 더 할까요? (1 ... 예 \0 ... 아니요) : ");
		scanf("%d", &retry);
	} while (retry == 1);

	return 0;
}

// ptr = 마지막 소수위치
// i = 현재 나누기에 쓰인 소수 위치