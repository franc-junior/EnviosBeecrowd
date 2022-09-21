import java.util.Collections;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
        
        int n = input.nextInt();
        for (int i = 0; i<n; i++){
            String vazio = "";
            int cont = 0;
            String palavra = input.nextLine();
            
            for(int x = 0; x<alfabeto.length; x++){
                int frequencia = Collections.frequency(, alfabeto[x]);
            }
        }
        
    }
    
}
