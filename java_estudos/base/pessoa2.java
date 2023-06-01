
import java.util.Calendar;
import java.util.Scanner;

/**
 *
 * @author Barbara
 */
public class Pessoa {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int dia = 0;
        int mês = 0;
        int ano_atual;
        int ano_nascimento = 0;
        int idade;
        
        String nome; 
        
    Calendar today = Calendar.getInstance();
    
      
        
   
                                        
    Scanner s = new Scanner(System.in);
    
    System.out.println("Digite o nome do usuário: ");
    nome = s.nextLine();
    System.out.println("Digite sua idade: ");
    idade = s.nextInt();
      
             
    calculaIdade(idade);
    
    informaIdade(idade);
    
    informaNome(nome);
    
    ajustaDataDeNascimento(dia, mês, ano_nascimento);
    
    
            
        
        
    }
    public static void calculaIdade(int idade){
    
    Calendar calendario = Calendar.getInstance();
        int ano_atual = calendario.get(Calendar.YEAR);
        int ano_nascimento = ano_atual - idade;
    
        System.out.println("Você nasceu em " +ano_nascimento + "\n");
        
    
    
      
        
      
        
    }
    
    public static void informaIdade(int idade){
        System.out.println("A idade atual do usuário é: "+idade);
    }
    
    public static void informaNome(String nome){
        System.out.println("O nome do usuário é: "+nome);
        
    }
    
    public static void ajustaDataDeNascimento(int dia, int mês, int ano_nascimento){
        
        System.out.println("---------------------------");
        System.out.println("Ajuste data de nascimento: ");
        
        Scanner s = new Scanner(System.in);
        
        System.out.println("Digite o dia de nascimento: ");
        dia = s.nextInt();
        System.out.println("Digite o mês de nascimento: ");
        mês = s.nextInt();
        System.out.println("Digite o ano de nascimento: ");
        ano_nascimento = s.nextInt();
        System.out.println("-----------------------------");
    }
    
    
    
    
}
