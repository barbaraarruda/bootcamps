package testacarro;


public class Carro {
    
    private int ano;
    private String marca;
    private String modelo;
    private boolean ligado;
    private int velocidade;
    public String cor;
    
    public void iniciar() {
        ligado = false;
        velocidade = 0;
    }

    public void ligar() {
        if (ligado == false) {
            System.out.println("Ligando...");
            ligado = true;
        }
    }

    public void desligar() {
        if (ligado == true && velocidade == 0) {
            System.out.println("Desligando...");
            ligado = false;
        }

    }

    public boolean getLigado() {
        return ligado;
    }

    public void acelerar() {
        if (ligado == true && velocidade < 240) {
            System.out.println("Acelerando...");
            velocidade += 10;
        }
    }

    public void freiar () {
        if (velocidade > 0) {
            System.out.println("acionando os freios...");
            velocidade -= 10;
        }
    }

    public int getVelocidade() {
        return velocidade;
    }

    public void setAno(int novoAno) {
        if (novoAno < 1000) {
            return;
        } else if (novoAno > 9999) {
            return;
        }
        ano = novoAno;
    }

    public int getAno() {
        return ano;
    }

    public void setMarca(String novaMarca) {
        marca = novaMarca;
    }

    public String getMarca() {
        return marca;
    }

    public void setModelo(String novoModelo) {
        modelo = novoModelo;
    }

    public String getModelo() {
        return modelo;
    }
    
    public String setCor(String novaCor){
        cor = novaCor;
        return null;
    }
    
    public String getCor(){
        return cor;
    }
    
}
