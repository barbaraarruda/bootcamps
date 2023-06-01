package testacarro;


public class TestaCarro {

        public static void main(String[] args) {
            
        Carro c1;
        c1 = new Carro();

        c1.setAno(2006);
        c1.setMarca("VW");
        c1.setModelo("Gol");

        c1.iniciar();

        c1.ligar();

        c1.acelerar();
        System.out.println("Velocidade do carro: " + c1.getVelocidade());

        c1.acelerar();
        System.out.println("Velocidade do carro: " + c1.getVelocidade());

        c1.freiar();
        c1.freiar();
        c1.desligar();
        
        Carro c2;
        c2 = new Carro();

        c2.setAno(2011);
        c2.setMarca("BMW");
        c2.setModelo("BMX");
        c2.setCor ("Azul");

        c2.iniciar();

        c2.ligar();

        c2.acelerar();
        System.out.println("Velocidade do carro: " + c1.getVelocidade());

        c2.acelerar();
        System.out.println("Velocidade do carro: " + c1.getVelocidade());

        c2.freiar();
        c2.freiar();
        c2.desligar();
        
        Carro c3;
        c3 = new Carro();

        c3.setAno(2019);
        c3.setMarca("YUK");
        c3.setModelo("BMX");
        c3.setCor ("Preto Metálico");

        c3.iniciar();

        c3.ligar();

        c3.acelerar();
        System.out.println("Velocidade do carro: " + c1.getVelocidade());

        c3.acelerar();
        System.out.println("Velocidade do carro: " + c1.getVelocidade());

        c3.freiar();
        c3.freiar();
        c3.desligar();
            }
    
}
