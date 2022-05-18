package pkg1043;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        float a = input.nextFloat(), b = input.nextFloat(), c = input.nextFloat();
        if ((a < b + c) & (b < a + c) & (c < a + b)){
            System.out.printf("Perimetro = %.1f\n", a+b+c);
        }else{
            System.out.printf("Area = %.1f\n", ((a+b)*c)/2);
        }
    }
    
}
