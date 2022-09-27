import java.io.IOError;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        ArrayList<String> lista;
        String tel, tel2;
        int cont, n, i;

        while(true){
            try{
                lista = new ArrayList<>();
                cont = 0;
                n = input.nextInt();
                for(i = 0; i<n; i++){lista.add(input.next());}
                Collections.sort(lista);

                tel = lista.get(0);
                
                for(i = 0; i<(n-1); i++){
                    tel2 = lista.get(i+1);

                    for(i = 0; i<tel.length(); i++){
                        if (tel.charAt(i) == tel2.charAt(i)){cont += 1;}
                        else{
                            tel = tel2;
                            break;
                        }
                    }
                }System.out.println(cont);
            }catch(IOError e){break;}
        }
    }
}
