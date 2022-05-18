package pkg1008;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int funcionario = inp.nextInt();
        int horas = inp.nextInt();
        double valorHora = inp.nextDouble();
        double salary = horas * valorHora;
        System.out.println("NUMBER = "+funcionario);
        System.out.printf("SALARY = U$ %.2f\n", salary);
    }
    
}
