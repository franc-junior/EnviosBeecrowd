package pkg1017;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double tempo = input.nextDouble();
        double veloc = input.nextDouble();
        double consumo = (tempo*veloc)/12; 
        System.out.printf("%.3f\n",consumo);
    }
    
}
