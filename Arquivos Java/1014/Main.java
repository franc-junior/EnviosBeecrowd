package pkg1014;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double x = input.nextDouble();
        double y = input.nextDouble();
        System.out.printf("%.3f km/l\n", x/y);
    }
    
}
