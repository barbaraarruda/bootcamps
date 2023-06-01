#include <stdio.h>

main (){ // Esse algoritmo irá resolver uma expressão matemática específica
	int a = 2;
	int b = 5;
	int c = 10;
	int result;
	result = b+c%a*(b-a/2);
	printf ("%d", result);
}
