package pkg1020;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int qDias = input.nextInt();
        
        int anos = 0; int meses = 0; int dias = 0;
        
        if (qDias >= 360) {anos = (qDias-(qDias%365))/365; qDias = qDias%365;}
        else {anos = 0;}
        
        if (qDias >= 30) {meses = (qDias-(qDias%30))/30; qDias = qDias%30;}
        else {meses = 0;}
        
        dias = qDias;
        
        System.out.println(anos+" ano(s)");
        System.out.println(meses+" mes(es)");
        System.out.println(dias+" dia(s)");
          
    }
    
}
