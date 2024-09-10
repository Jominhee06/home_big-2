#include <stdio.h>
#include <stdlib.h>
#include "mylntStack.h"

int Initialize(IntStack *s,int max)
{
	s->ptr = 0;
	if ((s->stk = calloc(max, sizeof(int))) == NULL) {
		s->max = 0;  // 배열 생성에 실패
		return -1;
	}
	s->max = max;
	return 0;
}
int Push(IntStack* s, int x)
{
	if (s->ptr >= s->max)  // 스택이 가득참
		return -1;
	s->stk[s->ptr++] = x;
	return 0;
}

int Pop(IntStack* s, int* x)
{
	if (s->ptr <= 0)
		return -1;
	*x = s->stk[--s->ptr];
	return 0;
}

int Peek(IntStack* s, int* x)
{
	if (s->ptr <= 0)
		return -1;
	*x = s->stk[s->ptr - 1];
	return 0;
}

void Clear(IntStack* s)
{
	s->ptr = 0;
}

int Capacity(const IntStack* s)
{
	return s->max;
}

int Size(const IntStack* s)
{
	return s->ptr;
}

int IsEmpty(const IntStack* s)
{
	return s->ptr <= 0;
}

int IsFull(const IntStack* s) 
{
	return s->ptr >= s->max;
}

int Search(const IntStack* s, int x)
{
	for (int i = s->ptr - 1; i >= 0; i--)   // 꼭대기 -> 바닥으로 선형 검색
		if (s->stk[i] == x)
			return i;    // 검색 성공
	return - 1;   // 검색 실패
}

void Print(const IntStack* s)
{
	int i;
	for (int i = 0; i < s->ptr; i++)
		printf("%d", s->stk[i]);
	putchar('\n');
}

void Terminate(IntStack* s)
{
	if (s->stk != NULL)
		free(s->stk);
	s->max = s->ptr = 0;
}