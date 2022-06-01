import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        String s = input.nextLine();
        String z = "zelda";

        String imprime = "Link Tranquilo";

        int contZ = 0;
        int i = 0;
        while(i<s.length()){
            char letra = Character.toLowerCase(s.charAt(i));
            char letraZ = z.charAt(contZ);
            if(letra == letraZ){
                contZ++;
                if(contZ == 5){
                    imprime = "Link Bolado";
                    break;
                }
            }else contZ = 0;
            i++;
        }System.out.println(imprime);
    }
}
