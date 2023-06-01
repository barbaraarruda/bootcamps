#include <stdio.h>
#include <stdlib.h>

main (){
	float imc, peso, altura; // Esse algoritmo vai calcular o imc do usuário e informar em qual categoria ela se encontra
	printf ("Esse programa vai calcular seu IMC\n\t");
	printf ("-------------------------------------\n");
	printf ("Digite aqui seu peso:  \n");
	scanf ("%2f", &peso);
	printf ("Digite aqui sua altura:  \n");
	scanf ("%2f", &altura);
	imc = peso/(altura*altura)*100;
	
	if (imc < 18,5){
		printf ("Voce esta abaixo do peso e seu imc: %.2f\n", imc);
	}else if (imc >= 18,5 && imc <=24,9){
			printf ("Voce esta com peso normal e seu imc: %.2f\n", imc);
		}else if (imc = 25,0 && imc <= 29,9){
			printf ("Voce esta com sobrepeso e seu imc: %.2f\n", imc);
		}else if (imc = 30 &&imc <= 34,9){
				printf ("Voce esta com obesidade grau I e seu imc: %.2f\n", imc);
			}else if (imc=35 && imc <= 39,9){
					printf ("Voce esta com obesidade grau II e seu imc: %.2f\n", imc);
				}else if (imc >= 40){
						printf ("Voce esta com obesidade grau III e seu imc: %.2f\n", imc);
					}
				}
		
