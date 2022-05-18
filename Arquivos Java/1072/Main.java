import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int dento = 0;
		int fora = 0;
		for(int i = 0; i<n; i++) {
			int valor = input.nextInt();
			if((valor>=10) && (valor<=20)) {dento++;}
			else {fora++;}
		}
		System.out.println(dento+" in");
		System.out.println(fora+" out");
	}
}
