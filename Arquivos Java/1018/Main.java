package pkg1018;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double din = input.nextDouble();
        double dinheiro = din;
        double cem = 0; double cinquenta = 0; double vinte = 0; double dez = 0; double cinco = 0; double dois = 0; double um = 0;
        
        
        if (dinheiro >= 100){cem = (dinheiro-dinheiro%100.0) /100.0; dinheiro=dinheiro%100.0;}
        if (dinheiro >= 50) {cinquenta = (dinheiro-dinheiro%50.0) /50.0; dinheiro=dinheiro%50.0;}
        if (dinheiro >= 20) {vinte = (dinheiro-dinheiro%20.0) /20.0; dinheiro=dinheiro%20.0;}
        if (dinheiro >= 10) {dez = (dinheiro-dinheiro%10.0) /10.0; dinheiro=dinheiro%10.0;}
        if (dinheiro >= 5) {cinco = (dinheiro-dinheiro%5.0) /5.0; dinheiro=dinheiro%5.0;}
        if (dinheiro >= 2) {dois = (dinheiro-dinheiro%2.0) /2.0; dinheiro=dinheiro%2.0;}
        if (dinheiro >= 1) {um = (dinheiro-dinheiro%1.0) /1.0; dinheiro=dinheiro%1.0;}
        
            
        System.out.printf("%.0f\n"
            + "%.0f nota(s) de R$ 100,00\n"
            + "%.0f nota(s) de R$ 50,00\n"
            + "%.0f nota(s) de R$ 20,00\n"
            + "%.0f nota(s) de R$ 10,00\n"
            + "%.0f nota(s) de R$ 5,00\n"
            + "%.0f nota(s) de R$ 2,00\n"
            + "%.0f nota(s) de R$ 1,00\n"
            , din, cem, cinquenta, vinte, dez, cinco, dois, um);
        
    }
    
}
