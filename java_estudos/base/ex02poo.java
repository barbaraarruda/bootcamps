package exercício02poo02;

//@author Barbara

public class exercício02POO02 {

    
    public static void main(String[] args) {
        Pessoa p1, p2;
        Conta c1, c2;
        c1 = new Conta();
        p1 = new Pessoa("Fulano", "fulano@gmail.com");
        p2 = new Pessoa(); 
        c2 = new Conta(190876, p1, 750.00f);
        
        p2.setNome("Ciclano");
        p2.setEmail("ciclano@gmail.com");
        
        
        c1.setCorrentista(p2);
        c1.setNumero(129876);
        c1.setSaldo(150.00f);
        
        System.out.println("O nome do correntista é: " + c1.getCorrentista().getNome());
        System.out.println("O número da conta é  " + c1.getNumero());
        System.out.println("O valor inicial da conta é:  " + c1.getSaldo());
        System.out.println("...............................");
        System.out.println("O nome do correntista é: " + c2.getCorrentista().getNome());
        System.out.println("O número da conta é  " + c2.getNumero());
        System.out.println("O valor inicial da conta é:  " + c2.getSaldo());
        
        
    }
    
}
    }
    
}
