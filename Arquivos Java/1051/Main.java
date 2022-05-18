package pkg1051;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        float n = input.nextFloat();
        float imposto = 0;
        float m = 0;
        
        if(n <= 2000.00){
            System.out.println("Isento");
        }else{
            n -= 2000.00;
            if(n <= 0){
                System.out.printf("R$ %.2f\n",imposto);
            }else{
                if(n > 1000.00){
                    m = 1000.00f;
                }else{
                    m = n;
                }
            }
            imposto += (8.00/100.00)*m;
            n -= 1000.00;
            if(n <= 0){
                System.out.printf("R$ %.2f\n",imposto);
            }else{
                if (n > 1500.00){
                    m = 1500.00f;
                }else{
                    m = n;
                }
                imposto += (18.00/100.00)*m;
                n -= 1500.00;
                if(n > 0){
                    imposto += (28.00/100.00)*n;
                    System.out.printf("R$ %.2f\n",imposto);
                }else{
                    System.out.printf("R$ %.2f\n",imposto);
                }
            }
        }
    } 
}
