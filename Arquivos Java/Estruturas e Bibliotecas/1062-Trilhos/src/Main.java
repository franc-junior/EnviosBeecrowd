import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> saida, estacao;
        int num=1, i, n, cont;
        String r;

        while (true){

            n = input.nextInt();
            if(n == 0){break;}

            while(true){
                saida = new ArrayList<>();
                for (i = 0; i<n; i++){
                    num = input.nextInt();
                    if (num == 0){
                        System.out.println();
                        break;
                    }
                    saida.add(num);
                }if (num == 0){break;}                                       //System.out.println(saida); System.out.println(chega);
                estacao = new ArrayList<>();
                estacao.add(0);
                cont = 0;
                r = "Yes";
                for (int sai : saida){
                    while (r != "No"){
                        if(sai == cont){
                            cont += 1;
                            break;
                        }else if(estacao.get(0) == sai){
                            estacao.remove(0);
                            break;
                        }else if((sai != cont) && (cont <= n)){
                            estacao.add(0, cont);
                            cont += 1;
                        }else{
                            r = "No";
                        }
                    }
                }System.out.println(r);
            }
        }
    }
}
