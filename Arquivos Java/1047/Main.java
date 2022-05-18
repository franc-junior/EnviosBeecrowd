package pkg1047;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int hi=input.nextInt(),mi=input.nextInt(),hf=input.nextInt(),mf=input.nextInt();
        int hora =((hf*60)+mf)-((hi*60)+mi);
        if (hora<=0){hora += (24*60);}
        System.out.printf("O JOGO DUROU %s HORA(S) E %s MINUTOS(S)\n",hora/60, hora%60);
    }
    
}
