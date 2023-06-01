#include <stdio.h>

main (){
	float nota1, nota2, media;
	printf ("Digite a primeira nota: ");
	scanf ("%f", &nota1);
	printf ("Digite a segunda nota: ");
	scanf ("%f", &nota2);
	media = (nota1 + nota2)/2;
	printf ("Resultado da media %.2f: ", media);
}
