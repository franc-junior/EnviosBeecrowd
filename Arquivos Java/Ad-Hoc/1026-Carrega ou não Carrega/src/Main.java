import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        long a, b;
        
        while(input.hasNext()){
            a = input.nextLong();
            b = input.nextLong();
            System.out.println(a^b);
        }
    }
}
