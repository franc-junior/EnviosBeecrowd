package pkg1042;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        List<Integer> lista = new ArrayList<Integer>(); //Lista 
        
        int a = input.nextInt(), b = input.nextInt(), c = input.nextInt();
        lista.add(a);lista.add(b);lista.add(c);
        
        Collections.sort(lista); // Ordenação da lista
       
        for (int i = 0; i<lista.size(); i++){
            System.out.println(lista.get(i)); // Impressão da lista
        }
        System.out.println("\n"+a+"\n"+b+"\n"+c);
    }
    
}
