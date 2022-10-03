import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        double menor=101, meno=0, migs;
        String[] osCaba = {"Otavio", "Bruno", "Ian", "Empate"};

        for(int i=0; i<3; i++){
            migs = input.nextDouble();
            if(migs < menor){
                menor = migs;
                meno = i;
            }else if(migs == menor){
                menor = migs;
                meno = 3;
            }
        }System.out.println(osCaba[(int) meno]);
    }
}
