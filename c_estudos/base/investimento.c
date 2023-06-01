#include <stdio.h>

int main(void)
{
int meses, counter;
float montante, investimento_mensal, rendimento = 0;

printf("Montante: ");
scanf("%f", &montante);
printf("Investimento Mensal: ");
scanf("%f", &investimento_mensal);
printf("Tempo em meses do investimento: ");
scanf("%d", &meses);

if((montante <= 0) || (investimento_mensal < 0) || (meses <= 0))
printf("\n \tMontante > 0 , Investimento Mensal > 0 ou = 0 , Meses > 0 ");
else
{
for( counter = 1; counter <= meses; counter++ )
{
rendimento += (montante * 0,0157);
montante *= 1.0157;
montante += investimento_mensal;
printf("\n \t No mes %d o montante e igual = %.2f ", counter, montante);
printf(" \t\t Rendimento = %.2f \n", rendimento);
}
}
}
