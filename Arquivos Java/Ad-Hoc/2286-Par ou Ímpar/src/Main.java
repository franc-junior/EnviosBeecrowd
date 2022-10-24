import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n=input.nextInt(), teste = 1,i, p1, p2;
        String j1, j2;

        while(n!=0){
            j1 = input.next();
            j2 = input.next();
            System.out.println("Teste "+teste);
            
            for(i =0; i<n; i++){
                p1 = input.nextInt();
                p2 = input.nextInt();
                if((p1+p2)%2==0){
                    System.out.println(j1);
                }else{
                    System.out.println(j2);
                }
            }teste++;
            System.out.println("");
            n=input.nextInt();
        }
    }
}