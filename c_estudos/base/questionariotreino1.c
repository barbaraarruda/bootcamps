#include <stdio.h>

main (){
	int num;
	printf ("Digite um numero: \n");
	scanf ("%d", &num);
	
	if(num==0){
		printf ("O numero e NULO\n");
	} else if (num<8){
		printf ("O numero e menor que 8\n");
		
	}else if (num<18){
		printf ("O numero e maior que 7\n");
		
	}else{
		printf ("O numero esta fora das condicoes criadas\n");
	}
}
