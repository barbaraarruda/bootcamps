#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>





int main ()
{
	int tabuada;
	printf ("\nDigite o numero 8 para prosseguir: \n");
	scanf ("%i", &tabuada);
	
	for(int x = 1; x<=10; ++x){
		printf ("%ix%i = %i\n", x, tabuada, x * tabuada);
	}
	
	return ;
	
}

