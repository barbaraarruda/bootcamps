#include<stdio.h>
#include<locale.h>

main (){
	setlocale(LC_ALL, "Portuguese"); // Esse algoritmo só irá imprimir a soma caso o valor seja maior que zero
	
	int n;
	int soma = 0;
	do {
	printf ("Digite um número positivo para ser somado ou negativo para sair:  \n");
	scanf ("%d", &n);
	if (n >= 0)
	soma = soma +n;	
	}while (n >= 0);
	printf ("A soma é %d\n", soma);
	printf ("Numero de valores digitados: %d", n);
	return 0;
	
	
	
	
	
}
