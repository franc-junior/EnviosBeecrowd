import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		int contPar = 0;
		int contImp = 0;
		int contPos = 0;
		int contNeg = 0;
		for(int i = 0; i<5; i++) {
			int valor = input.nextInt();
			if (valor%2 == 0) {contPar ++;}
			else {contImp ++;}
			if (valor>0) {contPos ++;}
			else if(valor<0) {contNeg ++;}
		}
		System.out.println(contPar+" valor(es) par(es)");
		System.out.println(contImp+" valor(es) impar(es)");
		System.out.println(contPos+" valor(es) positivo(s)");
		System.out.println(contNeg+" valor(es) negativo(s)");
	}
}