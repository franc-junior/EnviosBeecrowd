import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		int x = input.nextInt();
		if (x%2 == 0) {
			for(int i = x; i<=x+(6*2); i++) {
				if(i%2!=0) {
					System.out.println(i);
				}
			}
		}
		else {
			for(int i = x; i<=x+(6*2)-1; i+=2) {
				System.out.println(i);
			}
		}
	}
}
