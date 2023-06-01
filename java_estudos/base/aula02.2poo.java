package aula02poo;

/**
 *
 * @author Barbara
 */
public class Caneta {
    public String modelo;
    public String cor;
    private float ponta;
    protected int carga;
    private boolean tampada;
    public void status(){
        System.out.println("Modelo: " + this.modelo);
        System.out.println("A ponta é: " + this.ponta);
        System.out.println("Uma caneta " + this.cor);
        System.out.println("Carga é: " + this.carga);
        System.out.println("Está tampada? " + this.tampada);
    }
    
    public void rabiscar() {
        if (this.tampada == true){
            System.out.println("Erro! Não posso rabiscar, estou tampada");
        }else{
            System.out.println("Sucesso! Estou rabiscando");
        }
    }
    
   public void tampar(){
        this.tampada = true;
    }
    
    public void destampar(){
        this.tampada = false;
    }
}
