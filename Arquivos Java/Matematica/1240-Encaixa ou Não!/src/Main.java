import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String a, b;
        int n = input.nextInt(), la, lb;
        for (int i = 0; i<n; i++){
            a=input.next();
            b=input.next();
            la = a.length();
            lb = b.length();
            if((la>=lb) && (a.substring(la-lb).equals(b))){
                System.out.println("encaixa");}
            else{
                System.out.println("nao encaixa");}
        }
        
    }
}
