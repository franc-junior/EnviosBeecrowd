package pkg1036;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double a = input.nextDouble(); double b = input.nextDouble(); double c = input.nextDouble();
        double delta = ((b*b) - ((4*a*c)));
        double bask1 = (-b + Math.sqrt(delta))/(2*a); 
        double bask2 = (-b - Math.sqrt(delta))/(2*a); 
        if ((a == 0) || (delta < 0)){
            System.out.println("Impossivel calcular");
        }else{
            System.out.printf("R1 = %.5f\nR2 = %.5f\n", bask1, bask2);
        }
    }
    
}
