package pkg1021;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        double din = input.nextDouble();
        
        double cem = 0; double cinq = 0; double vinte = 0; double dez = 0; double cinco = 0; double dois = 0;
        double um = 0.0; double cinqC = 0.0; double vinteC = 0.0; double dezC = 0.0; double cincoC = 0.0; double umC = 0.0;
        
        cem = (din-(din%100.0))/100.0; din = din%100.0; 
        cinq = (din-(din%50.0))/50.0; din = din%50.0; 
        vinte = (din-(din%20.0))/20.0; din = din%20.0; 
        dez = (din-(din%10.0))/10.0; din = din%10.0; 
        cinco = (din-(din%5.0))/5.0; din = din%5.0; 
        dois = (din-(din%2.0))/2.0; din = din%2.0; 
        
        um = (din-(din%1.0))/1.0; din = din%1.0;
        cinqC = (din-(din%0.50))/0.50; din = (din%0.50)+0.001;
        vinteC = (din-(din%0.25))/0.25; din = (din%0.25)+0.001;
        dezC = (din-(din%0.10))/0.10; din = (din%0.10)+0.001;
        cincoC = (din-(din%0.05))/0.05; din = (din%0.05)+0.001;
        umC = (din-(din%0.01))/0.01; din = din%0.01;
        
        System.out.printf("NOTAS:\n"
                + "%.0f nota(s) de R$ 100.00\n"
                + "%.0f nota(s) de R$ 50.00\n"
                + "%.0f nota(s) de R$ 20.00\n"
                + "%.0f nota(s) de R$ 10.00\n"
                + "%.0f nota(s) de R$ 5.00\n"
                + "%.0f nota(s) de R$ 2.00\n"
                + "MOEDAS:\n"
                + "%.0f moeda(s) de R$ 1.00\n"
                + "%.0f moeda(s) de R$ 0.50\n"
                + "%.0f moeda(s) de R$ 0.25\n"
                + "%.0f moeda(s) de R$ 0.10\n"
                + "%.0f moeda(s) de R$ 0.05\n"
                + "%.0f moeda(s) de R$ 0.01\n",
                cem, cinq, vinte, dez, cinco, dois, um, cinqC, vinteC, dezC, cincoC, umC);
        
    }
    
}
