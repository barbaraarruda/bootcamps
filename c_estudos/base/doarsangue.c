#include <stdio.h>
 int main()
{
     int idade;
     printf("Digite sua idade: ");  
     scanf("%d", &idade);  
    
     if ( (idade < 18) || (idade > 67))  
        printf("Voce nao pode doar sangue\n");  
     else
        printf("Voce pode doar sangue\n");
}
