#include <stdio.h>
#include <stdlib.h>

main(){   
float peso , altura, imc;
printf("Informe seu peso em Kg:");
scanf ("%f",&peso);
printf("Informe sua altura em m:");
scanf ("%f",&altura);
imc = peso / (altura*altura);   
if (imc <19 ){
        printf("\n abaixo do peso");   
}else{       
if(imc >= 19 && imc<25){
            printf("\n  peso normal");       
}else{       
if(imc >= 25 && imc<30){
            printf("\n\t\t  sobrepeso");       
}else{       
if(imc >= 30 && imc<=40){
            printf("\n\t\t  obesidade grau I e II");       
}else{       
if (imc>40){
            printf("\n\t\t  obesidade grau IIi");
 } } } } }
    printf("\n\t\tSeu IMC é: %.2f",imc);

 system ("pause") ;
return 0;
}
