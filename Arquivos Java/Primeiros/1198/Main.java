import java.util.Scanner;
import java.util.NoSuchElementException;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		while(true) {
			try {
				long a = input.nextLong(), b = input.nextLong();
				System.out.println(Math.abs(a-b));
				
			}catch (NoSuchElementException e) {
				break;
			}
		}
		
	}

}
