/*
 Esse código é para aprender Java. É uma calculadora simples. 
 */
package videoaula;

import java.util.Scanner;

/**
 *
 * @author Barbara
 */
public class Videoaula {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int num1,num2,soma,sub,mult;
        
        float div; // em java, float representa os números reais.
                
        Scanner s = new Scanner (System.in); //ler os valores que vão ser inseridos pelo usuário
        
        System.out.println("Informe o primeiro numero: ");
        num1 = s.nextInt(); // vai ler o número inteiro e armazenar na variável num1
        System.out.println("Informe o segundo numero: ");
        num2 = s.nextInt(); // vai ler o próximo número digitado e guardar na variável num1
        
        soma = num1 + num2;
        
        System.out.println("A soma dos numeros é: "+soma);
        
        sub = num1 - num2;
        
        System.out.println("A subtração dos números é: "+sub);
        
        mult = num1 * num2;
        
        System.out.println("A multiplicação dos valores é: "+mult);
        
        div = (float) num1 / num2; //precisou forçar a máquina entender que precisa também pegar a parte fracionária, e não apenas a inteira. No caso, precisa de inserir o float.
        
        System.out.println("A divisão dos valores é: "+div);
    }
    
}
