#include <stdio.h>

main (){
	float not1, not2, soma; //Esse algoritmo irá calcular a média final da disciplina de Algoritmo e Estrutura de Dados
	printf ("Digite a primeira nota: ");
	scanf ("%f", &not1);
	printf ("Digite a segunda nota: ");
	scanf ("%f", &not2);
	soma = not1 + not2;
	if (soma >= 7) {
		printf ("Voce foi aprovado");
	} else {
		printf ("Voce foi reprovado");
		
	}
	}
