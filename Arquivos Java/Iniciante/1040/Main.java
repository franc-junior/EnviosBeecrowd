package pkg1040;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        double n1 = input.nextDouble();double n2 = input.nextDouble();double n3 = input.nextDouble();double n4 = input.nextDouble();
        
        double media = ((n1*2.0)+(n2*3.0)+(n3*4.0)+(n4))/10.0;
        System.out.printf("Media: %.1f\n",media-0.01);
        if (media>=7.0){System.out.println("Aluno aprovado.");}
        else if (media<5.0){System.out.println("Aluno reprovado.");}
        else {
            System.out.println("Aluno em exame.");
            double exame = input.nextDouble();
            System.out.println("Nota do exame: "+exame);
            double novaMedia = (media+exame)/2;
            if (novaMedia >= 5.0){System.out.println("Aluno aprovado.");}
            else{System.out.println("Aluno reprovado.");}
            System.out.printf("Media final: %.1f\n", novaMedia-0.01);
            
        }
    }
    
}