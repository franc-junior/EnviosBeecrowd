package pkg1045;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Double> lista = new ArrayList<Double>();
        double a = input.nextDouble(), b = input.nextDouble(), c = input.nextDouble();
        lista.add(a);
        lista.add(b);
        lista.add(c);
        Collections.sort(lista);
        a = lista.get(2);
        b = lista.get(1);
        c = lista.get(0);
        if(a>=(b+c)){System.out.println("NAO FORMA TRIANGULO");}
        else{
            if((a*a)==((b*b)+(c*c))){System.out.println("TRIANGULO RETANGULO");}
            else if((a*a)>((b*b)+(c*c))){System.out.println("TRIANGULO OBTUSANGULO");}
            else if((a*a)<((b*b)+(c*c))){System.out.println("TRIANGULO ACUTANGULO");}
            if(a==b && b==c){System.out.println("TRIANGULO EQUILATERO");}
            else if (((a == b) && (b != c)) || ((a == c) && (c != b)) || ((b == c)&& (c != a))){
                System.out.println("TRIANGULO ISOSCELES");
            }                 
        }            
    }  
}