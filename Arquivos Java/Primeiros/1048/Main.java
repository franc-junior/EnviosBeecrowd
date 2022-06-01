package pkg1048;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double salario = input.nextDouble();
        double porc = 0.0;
        double aumento = 0.0;
        if(salario <= 400.0){porc=0.15; aumento = salario * porc;}
        else if(salario <= 800.0){porc=0.12; aumento = salario * porc;}
        else if(salario <= 1200.0){porc=0.10; aumento = salario * porc;}
        else if(salario <= 2000.0){porc=0.07; aumento = salario * porc;}
        else if(salario > 2000.0){porc=0.04; aumento = salario * porc;}
        System.out.printf("Novo salario: %.2f\n" +
            "Reajuste ganho: %.2f\n" +
            "Em percentual: %.0f", salario+aumento, aumento, porc*100);
        System.out.println(" %");
        
    }
    
}
