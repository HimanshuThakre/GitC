#include<stdio.h>

void printaddress(int *n);  // Corrected function name

int main(){
    int n = 4;
    printaddress(&n);  // Corrected function name
    printf("address of n is : %u\n", &n);
    return 0;
}

void printaddress(int *n){  // Corrected function name
    printf("address of n is : %u\n",n);
}