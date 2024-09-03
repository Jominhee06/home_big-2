// 1.곱셈과 나눗셈을 실행한 횟수 코드

#include <stdio.h>

int main()
{
	int i, n;
	int prime[500];
	int ptr = 0;   // 마지막 소수가 저장된 위치 ptr+1 --> 소수개수
	unsigned long counter = 0;  // 연산 횟수
	prime[ptr++] = 2; // 초기 소수 2
	prime[ptr++] = 3;

	for (n = 5; n < 1000; n += 2) {   // n을 5부터 증가 시키면서 자기보다 작은 소수로 나누기
		int flag = 0;
		for (i = 1; counter++, prime[i] * prime[i] <= n; i++) {
			counter++;
			if (n % prime[i] == 0){
				flag = 1;
				break;
			}
		}
		if (! flag)
			prime[ptr++] = n;

		//if (ptr == i) prime[ptr++] = n;  // 마지막 소수(ptr)까지 했는데 없으면 지금수가 소수 
	}
	for (i = 0; i < ptr; i++) 
		printf("%d\n", prime[i]); 
	printf("곱셈과 나눗셈을 실행한 횟수 : %lu\n", counter);

	return 0;
}


// 2. 나눗셈을 실행한 횟수 코드

//#include <stdio.h>
//
//int main(void) {
//	int i, n;
//	int prime[500];
//	int ptr = 0; // ptr이 소수의 개수 역할(x+1번째 소수)
//
//	unsigned long counter = 0;
//	prime[ptr++] = 2;
//
//	//---------- n을 3부터 증가 시키면서 자기보다 작은 소수로 나누기 
//	for (n = 3; n <= 1000; n += 2) {
//		for (i = 0; i < ptr; i++) {
//			counter++;
//			if (n % prime[i] == 0) break;
//		}
//
//		if (ptr == i) prime[ptr++] = n; //마지막 소수(ptr)까지 했는데 없으면 지금수가 소수
//	}
//
//	for (i = 0; i < ptr; i++) printf("%d\n", prime[i]);
//
//	printf("나눗셈을실행한 횟수: %ul\n", counter);
//
//	return 0;
//}