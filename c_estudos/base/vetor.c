#include <stdio.h>
#include <stdlib.h>

int main() // esse algoritmo vai ler 15 valores e armazenar em vetor, depois imprimir. 
{
	float valores[15];
	int indice;
	printf ("Lendo os valores:\n");
	for (indice=0; indice<15; indice++){
		printf ("Digite o proximo valor desejado: ");
		scanf("%f", &valores[indice]);
	} //finalizando o bloco do for
	printf ("Exibindo os valores digitados: \n");
	for (indice=0; indice<15; indice++){
		printf ("O valor %f foi armazenado na posicao %d do vetor. \n", valores[indice], indice);
		
	} //finalizando o bloco do for
	system("pause");
}
