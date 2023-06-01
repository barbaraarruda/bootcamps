package testalampada;

public class Lampada {
   public boolean ligada;

   
    public void ligar(){
        if (this.ligada == true){
            System.out.println("A lâmpada está acesa");
            
        }else{
            System.out.println("A lâmpada está apagada");
        }
    }
    
    public void acender (){
        this.ligada = true;
    }
    
    public void apagar (){
        this.ligada = false;
    }
    
    public void status (){
        System.out.println("A lâmpada está "+this.ligada);
    }
    
    }
