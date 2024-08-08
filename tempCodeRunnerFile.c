#include<stdio.h>

void dowork(int a, int b, int *sum, int *prod, int *avg);

int main() 
{
    int a = 3, b = 5;
    int sum, prob, avg;
    dowork(a, b, &sum, &prob, &avg);

    printf("sum = %d, prob = %d, avg = %d", sum, prob, avg);
    return 0;
}
 void dowork(int a, int b, int *sum, int *prod, int *avg)
 {
    *sum = a+b;
    *prod = a*b;
    *avg = (a+b)/2;
 }