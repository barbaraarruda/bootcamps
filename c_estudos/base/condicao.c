#include <stdio.h>
#include <locale.h>

main (){
	setlocale(LC_ALL, "Portuguese"); // Esse algoritmo irá imprimir a soma de números positivos apenas se o usuário digitar um número negativo
	int x, maior=0, soma=0;
	do{
		printf("Digite um valor positivo [Negativo para Sair]: ");
		scanf("%d", &x);
		if(x>0){
			soma=soma+x;
			if(x>maior){
				maior=x;
			}
		}
	}
	while(x>=0);
	printf("Soma dos Numeros: %d", soma);
	
}
