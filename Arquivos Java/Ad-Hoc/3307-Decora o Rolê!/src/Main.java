import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        for (int i = 0; i< n; i++){
            int a = input.nextInt();
            double r = Math.sqrt(a/(3.14*4));
            if(r <= 12){
                System.out.printf("vermelho = R$ %.2f\n",a*0.09);
            }else if(r<=15){
                System.out.printf("azul = R$ %.2f\n",a*0.07);
            }else{
                System.out.printf("amarelo = R$ %.2f\n",a*0.05);
            }
        }
           
    }
    
}