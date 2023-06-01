package aula02poo;

/**
 *
 * @author Barbara
 */
public class Aula02POO {
   
    public static void main(String[] args) { //forma de programar - naturalidade
       Caneta c1  = new Caneta();
       c1.cor = "Azul"; // referência a atributo
       c1.ponta = 0.5f;
       c1.tampar();
       
       c1.rabiscar();
       c1.status(); // referência a método
       
       Caneta c2 = new Caneta();
       c2.modelo = "Hostnet";
       c2.cor = "Preta";
       c2.destampar();
       c2.rabiscar();
       c2.status();
       
    }
    
}
