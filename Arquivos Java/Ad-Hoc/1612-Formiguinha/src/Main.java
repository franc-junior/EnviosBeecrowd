import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        
        for(int i = 0; i<t; i++){
            double n = input.nextInt();
            
            System.out.println(Math.round((n/2)));
        }
    }
}