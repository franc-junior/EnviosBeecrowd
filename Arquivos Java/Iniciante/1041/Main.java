package pkg1041;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        float y = input.nextFloat(); float x = input.nextFloat();
        String q = "Origem";
        if (y > 0){
            if (x > 0){q = "Q1";}
            else if (x < 0){q = "Q4";}
            else{q = "Eixo X";}
        }
        else if (y < 0){
            if (x > 0){q = "Q2";}
            else if (x < 0){q = "Q3";}
            else{q = "Eixo X";}
        }
        else if (y == 0){
            if (x > 0){q = "Eixo Y";}
            else if (x < 0){q = "Eixo Y";}
            else{q = "Origem";}
        }
        System.out.println(q);
    }
    
}
