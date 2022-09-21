package pkg1044;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt(), b = input.nextInt();
        if (a>b){
            if (a%b == 0){System.out.println("Sao Multipolos");}
            else{System.out.println("Nao Sao Multiplos");}  
        }else if (b>a){
            if (b%a == 0){System.out.println("Sao Multiplos");}
            else{System.out.println("Nao Sao Multiplos");}
        }else{System.out.println("Sao Multiplos");}
    }
    
}
