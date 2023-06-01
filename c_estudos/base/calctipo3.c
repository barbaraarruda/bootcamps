#include <stdio.h>

int main(void)
{
float num1,num2;
char option;

do
{
system("clear||cls");
printf("\t\tCalculadora:\n");
printf("+ < Para somar\n- < para subtrair\n* < para multiplicar\n/ < para dividir\n%% < Modulo da divisao\n");
printf("Para fechar a calculadora, apenas coloque 0 no lugar da operacao.\n");
printf("Digite a conta que deseja fazer.(Exemplo: 10 * 2):\n");
scanf("%f %c %f",&num1,&option,&num2);

switch(option)
{
case '+':
printf("%.2f + %.2f = %.2f\n",num1,num2,(num1+num2));
system("pause");
break;
case '-':
printf("%.2f - %.2f = %.2f\n",num1,num2,(num1-num2));
system("pause");
break;
case '*':
printf("%.2f * %.2f = %.2f\n",num1,num2,(num1*num2));
system("pause");
break;
case '/':
if(num2==0||num1==0)
printf("Nao existe divisao por 0\n");
else
printf("%.2f / %.2f = %.2f\n",num1,num2,(num1/num2));
system("pause");
break;
case '%': 
printf("%.2f %% %.2f = %.2f\n",num1,num2,(int)num1%(int)num2);
system("pause");
break;

default:
if(option!='0')
printf("Operaçao invalida!\n");
else
{
printf("Fechando Calculadora!\n");
return 0;
}
system("pause");
break;
}
}while(option);
}
