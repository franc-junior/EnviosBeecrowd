import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n, j, i, mary, john;
        
        while(true){
            n = input.nextInt();
            if(n == 0){
                break;
            }else{
                mary = 0;
                john = 0;
                for(i=0;i<n;i++){
                    j = input.nextInt();
                    if(j == 0){
                        mary++;
                    }else{
                        john++;
                    }
                }System.out.printf("Mary won %d times and John won %d times\n",mary, john);
            }
        }
    }
}