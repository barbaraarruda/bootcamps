#include <stdio.h>
#include <stdlib.h>

int main()
{
	float notas[5];
	int indice;
	float soma;
	float media;
	
	printf ("Lendo as notas:\n");
	
	for (indice=0; indice<5; indice++){
		printf("Digite a proxima nota do aluno: ");
		scanf("%f", &notas[indice]);
	} //finalizando o bloco do for
	printf("Exibindo as notas digitadas: \n");
	
	for (indice=0; indice<5; indice++){
	printf ("A nota %f foi armazenada na posicao %d do vetor.\n", notas[indice], indice);
	
	}//finalizando o bloco do for
	for (indice=0; indice<5; indice++){
		printf ("Digite enter para prosseguir:\n");
		soma = soma + notas[indice];
		
	}
	media = soma / 5;
	printf ("A soma e: %f\n", soma);
	printf ("A media e: %f\n", media);
		
	system("pause");
	return 0;
		
}
