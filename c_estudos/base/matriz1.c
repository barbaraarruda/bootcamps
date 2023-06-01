#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main(){ // esse algoritmo irá fazer as especificidades exigidas de uma matriz 3x3 da lista de revisão
 int i, j, m[3][3];
 //captura os elementos
 for(i=0;i<3;i++)
 for(j=0;j<3;j++){
 printf("Elemento[%d][%d]= ",i,j);
 scanf("%d",&m[i][j]);
 }
 
 //exibe valores originais
 printf("\n::: Valores Originais :::\n");
 for(i=0;i<3;i++){
 for(j=0;j<3;j++)
 printf("%d ",m[i][j]);
 printf("\n");
 }
 
 //exibe a diagonal principal digitada
 for(i=0;i<3;i++){
 	for(j=0;j<3;j++){
 		if(i == j){
 			printf("%5d", m[i][j]);
		 }
	 }
 }
 
 //multiplica por 2
 for(i=0;i<3;i++)
 for(j=0;j<3;j++)
 m[i][j]=m[i][j]*2;
 
 //exibir valores multiplicados
 printf("\n::: Valores Multiplicados por 2:::\n");
 for(i=0;i<3;i++){
 for(j=0;j<3;j++)
 printf("%d ",m[i][j]);
 printf("\n");
 }
 return 0;
}
