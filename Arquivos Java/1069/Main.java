package pkg1069;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        
        for (int j = 0; j < n; j ++){
        
            String peneira = input.next();
            int soma = 0;
            int cont = 0;
            char abre = '<';
            char fecha = '>';
            
            for (int i = 0; i <= peneira.length()-1; i ++){
                char peneiraChar = peneira.charAt(i);
                
                if (abre == peneiraChar || fecha == peneiraChar){
                    if (abre == peneiraChar){cont ++;}
                    
                    else{soma ++; cont --;}
                }
            }
        System.out.println(soma);
        }
    }
}