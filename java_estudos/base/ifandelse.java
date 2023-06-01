/*
 * Esse código ensina sobre estruturas de condição e decisão Se e Senão - IF e ELSE
 * Vídeo aula 06 do canal Java Plugados
 */
package ifeelse;

import java.util.Scanner;

/**
 *
 * @author Barbara
 */
public class IFeELSE {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        int num1,num2,soma;
        
        
                
        Scanner s = new Scanner (System.in); //instância do objeto - método de leitura de dados
        
        System.out.println("Informe o primeiro numero: ");
        num1 = s.nextInt(); // vai ler o número inteiro e armazenar na variável num1
        System.out.println("Informe o segundo numero: ");
        num2 = s.nextInt(); // vai ler o próximo número digitado e guardar na variável num1
        
        soma = num1 + num2;
        
        // Estruturas de condição
        
        if(soma > 10 ){ //estrutura de condição se
           System.out.println("A soma é maior que 10. O valor da soma é: "+soma);
        }
        else if(soma < 10){ // estrutura de condição senão se
            System.out.println("A soma é menor que 10. O valor da soma é: "+soma);
        }
        else{ //estrutura de condição senão
            System.out.println("A soma é igual a 10");
        }
    }
    
}
