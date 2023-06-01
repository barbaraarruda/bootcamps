#include <stdio.h>

main(){
    float soma=1, numero, quantidade_Numero=0;
     while (numero != -1){
        printf("Digite um numero : ");
        scanf ("%f",&numero);
        
        soma += numero;
        quantidade_Numero++;

    }
    printf("%.2f", soma);
    printf("\nQuantidade de numeros %.0f", quantidade_Numero-1);
    

}
