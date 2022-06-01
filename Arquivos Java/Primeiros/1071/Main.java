import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		int x = input.nextInt();
		int y = input.nextInt();
		int maior = y;
		int menor = x;
		int soma = 0;
		if(x>y) {maior = x; menor = y;}
		for(int i = menor+1; i<maior; i++) {
			if(i%2 != 0) {
				soma+=i;
			}
		}
		System.out.println(soma);
	}

}
