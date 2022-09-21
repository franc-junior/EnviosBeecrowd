import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        int soma, i, j, calculo, maior = 0;
        double decimal;
        String binary = "", binaryInverso;
        
        for(j=0; j<4; j++){
            soma = 0;
            for(i=0; i<7; i++){soma += input.nextInt();}
            if(soma>maior){maior = soma;}
        }

        decimal = maior;
        while (decimal>0){
            if(decimal%2 == 0){binary+="0";}
            else{binary+="1";}
            calculo = (int)decimal/2;
            decimal = calculo;
        }
        binaryInverso = new StringBuilder(binary).reverse().toString();
        System.out.println(maior+" = "+binaryInverso);
    }
}
