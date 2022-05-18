import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner input = new Scanner(System.in);
		String d1 = input.nextLine();
		String[] str1 = d1.split(" ");
		int dias1 = Integer.parseInt(str1[1]);
		String valor1 = input.nextLine();
		String[] parts1 = valor1.split(" : ");
		int hora1 = Integer.parseInt(parts1[0]);
		int minu1 = Integer.parseInt(parts1[1]);
		int segu1 = Integer.parseInt(parts1[2]);
		
		String d2 = input.nextLine();
		String[] str2 = d2.split(" ");
		int dias2 = Integer.parseInt(str2[1]);
		String valor2 = input.nextLine();
		String[] parts2 = valor2.split(" : ");
		int hora2 = Integer.parseInt(parts2[0]);
		int minu2 = Integer.parseInt(parts2[1]);
		int segu2 = Integer.parseInt(parts2[2]);
		
		int dias = dias2 - dias1;
		int horas = hora2 - hora1;
		int minutos = minu2 - minu1;
		int segundos = segu2 - segu1;
		
		if (segundos < 0){
			minutos --;
			segundos += 60;
		}
		if (minutos < 0){
			horas --;
			minutos += 60;
		}
		if (horas < 0){
			dias --;
			horas += 24;
		}
		System.out.println(dias+" dia(s)");
		System.out.println(horas+" hora(s)");
		System.out.println(minutos+" minuto(s)");
		System.out.println(segundos+" segundo(s)");
			
	}
}
