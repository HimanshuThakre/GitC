#include<stdio.h>

void pirntaddress(int *n);

int main(){
    int n = 4;
   pirntaddress(&n);
    printf("address of n is : %u\n", &n);
    return 0;
}

void pirntaddress(int *n){
    printf("address of n is : %u\n", n);
}


