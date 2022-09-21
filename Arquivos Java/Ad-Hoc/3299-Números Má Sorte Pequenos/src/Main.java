import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String treze = "13";
        String n = input.nextLine();
        if (n.contains(treze)){
            System.out.println(n+" es de Mala Suerte");
        }else{
            System.out.println(n+ " NO es de Mala Suerte");
        }
    }
    
}
