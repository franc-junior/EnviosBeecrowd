import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		float soma = 0;
		int cont = 0;
		for (int i=0; i<6; i++) {
			float valor = input.nextFloat();
			if (valor>0) {
				soma += valor;
				cont ++;
			}
		}
		System.out.printf("%d valores positivos\n%.1f",cont, soma/cont);
	}
}
