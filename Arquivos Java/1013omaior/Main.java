package pkg1013omaior;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        
        int maiorAB = ((a+b)+(a-b))/2;
        int maiorABC = ((maiorAB+c)+(maiorAB-c))/2;
        System.out.println(maiorAB);
        
    }
    
}
