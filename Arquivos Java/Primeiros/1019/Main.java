package pkg1019;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double n = input.nextDouble();
        
        double segundos = 0; double minutos = 0;
           
        if (n >= 60){segundos = n%60; n = (n-(n%60))/60;}
        else {segundos = n; n=0;}
        
        if (n >= 60){minutos = n%60; n = (n-(n%60))/60;}
        else{minutos = n; n=0;}
        
        double horas = n;
        
        System.out.printf("%.0f:%.0f:%.0f\n", horas, minutos, segundos);
    }
    
}

