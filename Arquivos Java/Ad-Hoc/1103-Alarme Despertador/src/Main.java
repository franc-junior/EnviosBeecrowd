import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        int h1, m1, h2, m2, h;
        
        while(true){
            h1 = input.nextInt();
            m1 = input.nextInt();
            h2 = input.nextInt();
            m2 = input.nextInt();
            
            if ((h1+h2+m1+m2) == 0){break;}
            h = ((h2*60)+m2)-((h1*60)+m1);
            if(h<0){
                h = (24*60)+h;
            }System.out.println(h);
        }
    }
}