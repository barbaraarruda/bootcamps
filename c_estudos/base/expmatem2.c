#include <stdio.h>

main (){ // esse algoritmo irá resolver uma expressão matemática específica. 
	int a = 2;
	int b = 5;
	int c = 10;
	int result;
	result = (b+c)%2+a*(b+(c*4));
	printf ("%d", result);
}
