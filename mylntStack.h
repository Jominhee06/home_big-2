#ifndef __IntStack
#define __lntStack

typedef struct {
	int max;  // 배열 크기
	int ptr;  //저장된 자료개수
	int* stk; // 배열 주소
}IntStack;

//초기화
int Initialize(IntStack* s, int max);

int push(IntStack* s, int x);

int Pop(IntStack* s, int *x);

int Peek(const IntStack* s, int *x);

void Clear(IntStack* s);

int Capacity(const IntStack* s);

int Size(const IntStack* s);

int IsEmpty(const IntStack* s);

int IsFull(const IntStack* s);

int Search(const IntStack* s, int x);

void Print(const IntStack* s);

void Terminate(IntStack* s);

#endif 

