#include<stdio.h>
void square(int n);

void _square(int * n);
int main() {
    int number = 4;
    square(number);
    printf("%d", number);

    _square(&number);
    printf("%d\n", number);

   return 0;
}
   
void square(int n) {
   n = n * n;
   printf("%d \n", n);
}

void _square(int* n) {
   *n = (*n) * (*n);
   printf("%d\n", *n);
   }
