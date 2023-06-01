#include <stdio.h>
void main(){ // esse algoritmo usou vetor para armazenar os 6 números inteiros requeridos.
int A[] = { 1,0,5,-2,-5,7 };
int i;
printf("%d %d %d \n", A[0], A[1], A[5]);
A[4] = 100;
for (i=0;i<5;i++){
printf("%d\n", A[i]);
};
}
