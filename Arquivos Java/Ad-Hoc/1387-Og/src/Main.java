import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int l; int r;
        while(true){
            l = input.nextInt();
            r = input.nextInt();
            if((l == 0) && (r == 0)){
                break;
            }
            System.out.println(l+r);
        }
    }
}
