import java.util.Scanner;
import java.lang.Integer;
public class Main{
	
	public static void main(String[]args) {
		
		Scanner input = new Scanner(System.in);
		int n = Integer.parseInt(input.nextLine());
		
		for(int i = 0; i<n; i++) {
			String string = input.nextLine();
			int tamanhoM = string.length()/2;
			StringBuilder str1 = new StringBuilder(string.substring(0,tamanhoM));
			StringBuilder str2 = new StringBuilder(string.substring(tamanhoM));
			System.out.printf("%s%s\n",str1.reverse(),str2.reverse());
			
		}
	}
}

