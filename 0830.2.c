#include <stdio.h>
#include <string.h>
#include <stdlib.h> // # -> 전처리기

int main()
{
	char s1[11] = "23@45@67#50";  // s1 = 시작 주소 저장
	char* ptr = strtok(s1, "@#");  // strtok = 문자열을 분리해주는 역할 함수
	int num[5];    // 배열공간에 형변환한 데이터를 저장
	int str = 0;   // 배열 인덱스를 구분하기 위해 만든 저장 공간

	while (ptr != NULL) // ptr이 널이 아닌경우 반복해서 실행한다.
	{
		num[str] = atoi(ptr); // atoi = 문자 스트링을 정수값으로 변환하는 함수, ptr은 쪼개진 첫번째 문자열을 가지고 있다.
		//printf("%s\n", ptr);
		printf("%d\n", num[str]); // num에 저장한 str의 데이터를 출력
		str++; // str이 후위형 증가
		ptr = strtok(NULL, "@#");  // NULL = 시작주소
	}
	return 0; // 반환하는 함수
}

// static = 하나의 내부파일로 제한