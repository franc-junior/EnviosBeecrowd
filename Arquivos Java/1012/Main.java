package pkg1012;

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Digite aqui:");
        double a = input.nextDouble(); 
        System.out.print("Digite aqui:");
        double b = input.nextDouble(); double c = input.nextDouble();
        double triangulo = (a*c)/2;
        double circulo = (c*c)*3.14159d;
        double trapezio = ((a+b)*c)/2;
        double quadrado = b*b;
        double retangulo = a*b;
        System.out.printf("TRIANGULO: %.3f\n", triangulo);
        System.out.printf("CIRCULO: %.3f\n", circulo);
        System.out.printf("TRAPEZIO: %.3f\n", trapezio);
        System.out.printf("QUADRADO: %.3f\n", quadrado);
        System.out.printf("RETANGULO: %.3f\n", retangulo);
    }
    
}
