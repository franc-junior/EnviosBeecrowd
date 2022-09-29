import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String notas;
        String[] notasSeparadas;
        double soma, num;
        int certo;
         
        while (true){
            notas = input.nextLine();
            if(notas.equals("*")){break;}
            notasSeparadas = notas.split("/");
            
            certo = 0;
            for(String i : notasSeparadas){
                soma = 0;

                for(int j = 0; j<i.length(); j++){
                    if(i.charAt(j) == 'W'){
                        num = 1;
                    }else if(i.charAt(j) == 'H'){
                        num = 1.0/2.0;
                    }else if(i.charAt(j) == 'Q'){
                        num = 1.0/4.0;
                    }else if(i.charAt(j) == 'E'){
                        num = 1.0/8.0;
                    }else if(i.charAt(j) == 'S'){
                        num = 1.0/16.0;
                    }else if(i.charAt(j) == 'T'){
                        num = 1.0/32.0;
                    }else{
                        num = 1.0/64.0;
                    }soma += num;

                }if (soma == 1){
                    certo += 1;
                }
            }System.out.println(certo);
        }
    }
}