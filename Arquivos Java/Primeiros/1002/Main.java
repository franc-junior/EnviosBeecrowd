package pkg1002;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double pi = 3.14159;
        double raio = input.nextDouble();
        System.out.printf("A=%.4f\n", (raio*raio)*pi);
    }   
}
