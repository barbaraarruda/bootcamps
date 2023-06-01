/*
 Esse algoritmo serve para aprender a usar métodos. 
 */
package videoaula11;

import java.util.Scanner;

/**
 *
 * @author Barbara
 */
public class VideoAula11 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int num1,num2,sub;
        
        float div; // em java, float representa os números reais.
                
        Scanner s = new Scanner (System.in); //ler os valores que vão ser inseridos pelo usuário
        
        System.out.println("Informe o primeiro numero: ");
        num1 = s.nextInt(); // vai ler o número inteiro e armazenar na variável num1
        System.out.println("Informe o segundo numero: ");
        num2 = s.nextInt(); // vai ler o próximo número digitado e guardar na variável num1
        
        somar (num1, num2);
        
        sub = subtracao(num1, num2);
        System.out.println("A subtração é: "+sub);
        
        multiplicar (num1, num2);
        
        
        
    }
    // declaração de métodos
    
    //método sem retorno de dados - executa e já mostra o valor. 
    
    public static void somar(int num1, int num2){ //void porque não há retorno. Atenção: sempre tem que fazer a chamada de métodos ou o método não aparece no programa
        int soma;
        soma = num1 + num2;
        System.out.println("A soma é: "+soma);
    }
    
    //método com retorno - retorna na classe principal. 
    public static int subtracao(int num1, int num2){
        int sub;
        sub = num1 - num2;
        return sub;
    }
    
    public static void multiplicar(int num1, int num2){ //void porque não há retorno. Atenção: sempre tem que fazer a chamada de métodos ou o método não aparece no programa
        int mult;
        mult = num1 * num2;
        System.out.println("A soma é: "+mult);
    }
    
}   
