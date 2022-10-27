import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int x1, y1, x2, y2, i, dx1, dy1, dx2, dy2, dx3, dy3, dx4, dy4;
        
        while (true){
            x1 = input.nextInt();
            y1 = input.nextInt();
            x2 = input.nextInt();
            y2 = input.nextInt();
            if(x1+x2+y1+y2 == 0){
                break;
            }else if ((x2==x1) && (y2==y1)){
                System.out.println(0);
            }
            else if (x2==x1 || y2==y1){
                System.out.println(1);
            }
            else{
                i = 1;
                while(true){
                    dx1 = (x1-i);
                    dy1 = (y1-i);

                    dx2 = (x1-i);
                    dy2 = (y1+i);

                    dx3 = (x1+i);
                    dy3 = (y1-i);

                    dx4 = (x1+i);
                    dy4 = (y1+i);

                    i+=1;

                    if (i > 8){ 
                        System.out.println(2);
                        break;
                    }else if ((x2 == dx1) && (y2 == dy1)){
                        System.out.println(1);
                        break;
                    }else if ((x2 == dx2) && (y2 == dy2)){
                        System.out.println(1);
                        break;
                    }else if ((x2 == dx3) && (y2 == dy3)){
                        System.out.println(1);
                        break;
                    }else if ((x2 == dx4) && (y2 == dy4)){
                        System.out.println(1);
                        break;
                    }
                }
            }
        }
    }
}