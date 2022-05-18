package pkg1038;

import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Dictionary<Integer, Double> dic = new Hashtable<Integer, Double>();
            dic.put(1,4.0);
            dic.put(2,4.5);
            dic.put(3,5.0);
            dic.put(4,2.0);
            dic.put(5,1.5);
        int cod = input.nextInt(); int qtd = input.nextInt();
        double total = dic.get(cod)*qtd;
        System.out.printf("Total: R$ %.2f\n",+total);
        
    }
    
}
