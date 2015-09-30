#include <stdio.h>

void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i=size-1;i>=0;i--)
    {
        for (j=7;j>=0;j--)
        {
            byte = b[i] & (1<<j);
            byte >>= j;
            printf("%u", byte);
        }
    }
    puts("");
}

void printb(char* title, int num){
	printf("%s:", title);
	printBits(sizeof(num), &num);
}

int updateBits(int n, int m, int i, int j){

	int left = ~0 << (j+1);

	int right = ((1<<i) - 1);

	int mask = left | right;

	// printb("mask", mask);

	int n_cleared = n & mask;

	// printb("n_cleared", n_cleared);

	int m_shifted = m << i;

	return n_cleared | m_shifted;
}

void main(){

	// printf("Hello World!");

	int n = 1024;
	printb("n", n);

	int m = 19;
	printb("m", m);

	int i = 2;
	printf("i:%d\n", i);

	int j = 6;
	printf("j:%d\n", j);

	int y = updateBits(n, m, i, j);
	// printf("%d\n\r", y);
	printb("y", y);
}