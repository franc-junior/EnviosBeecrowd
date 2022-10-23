import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        int n, q, x, y, i, borb;
        ArrayList matriz = new ArrayList(), linha, borboletas, m;
        
        n = input.nextInt();
        for(i = 0; i<n; i++){
            linha = new ArrayList();
            for(int lin = 0; lin<n; lin++){
                linha.add(input.nextInt());
            }matriz.add(linha);
        }borboletas = new ArrayList();
        q = 0;
        for(i = 0; i<(n*2); i++){
            x = input.nextInt();
            y = input.nextInt();
            m = (ArrayList) matriz.get(x-1);
            borb = (int) m.get(y-1);           
            if(!borboletas.contains(m.get(y-1))){
                borboletas.add(borb);
                q+=1;
            }
        }System.out.println(q);
    }
}