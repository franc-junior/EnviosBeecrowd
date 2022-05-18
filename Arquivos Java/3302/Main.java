package pkg3302;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        for (int i = 0; i<n; i++){
            int num = input.nextInt();
            System.out.printf("resposta %s: %s\n", i+1, num);
        }
        
    }
    
}
