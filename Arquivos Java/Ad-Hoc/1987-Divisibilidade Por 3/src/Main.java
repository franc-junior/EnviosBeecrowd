import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n, i, s;
        String m;
        
        while(input.hasNext()){
            n = input.nextInt();
            m = input.next();
            s = 0;
            
            for(i=0;i<n;i++){
                s += Integer.parseInt(String.valueOf(m.charAt(i)));
            }
            if(s%3 == 0){
                System.out.println(s+" sim");
            }else{
                System.out.println(s+" nao");
            }
        }
        
    }
}