package pkg1046;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int inicial = input.nextInt(), fim = input.nextInt();
        int h = fim-inicial;
        if(h<=0){h += 24;}
        System.out.println("O JOGO DUROU "+h+" HORA(S)");       
    }
}
