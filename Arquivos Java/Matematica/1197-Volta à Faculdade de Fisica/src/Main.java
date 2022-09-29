import java.util.Scanner;


public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        while(input.hasNext()){
                int v = input.nextInt();
                int t = input.nextInt();
                System.out.println((v*t)*2);        
 
        }input.close();
    }
}