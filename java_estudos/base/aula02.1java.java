package aula02poo;

/**
 *
 * @author Barbara
 */
public class Caneta {
    String modelo;
    String cor;
    float ponta;
    int carga;
    boolean tampada;
    void status(){
        System.out.println("Modelo: " + this.modelo);
        System.out.println("A ponta é: " + this.ponta);
        System.out.println("Uma caneta " + this.cor);
        System.out.println("Carga é: " + this.carga);
        System.out.println("Está tampada? " + this.tampada);
    }
    
    void rabiscar() {
        if (this.tampada == true){
            System.out.println("Erro! Não posso rabiscar, estou tampada");
        }else{
            System.out.println("Sucesso! Estou rabiscando");
        }
    }
    
    void tampar(){
        this.tampada = true;
    }
    
    void destampar(){
        this.tampada = false;
    }
}
