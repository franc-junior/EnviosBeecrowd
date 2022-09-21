import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		for(int i = 2; i<=n; i+=2) {
			System.out.println(i+"^2 = "+(i*i));
		}
	}
}
