import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String a = input.nextLine();
        if (a.length()<=140){System.out.println("TWEET");}
        else {System.out.println("MUTE");}
    }
}
