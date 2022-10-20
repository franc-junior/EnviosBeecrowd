import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        int n, g, pontos, s, r, i, j, p;
        ArrayList otos;
        
        while(input.hasNext()){
            otos = new ArrayList();
            n = input.nextInt();
            g = input.nextInt();
            pontos = 0;
            
            for(i = 0; i<n; i++){
                s = input.nextInt();
                r = input.nextInt();
                if(s==r){
                    if(g>=1){
                        g-=1;
                        pontos+=3;
                    }else{
                        pontos+=1;
                    }
                }else if(s>r){
                    pontos+=3;
                }else{
                    otos.add(r-s);
                }
            }Collections.sort(otos);
            for(j = 0; j<otos.size(); j++){
                p = (int) otos.get(j);
          
                if (g>p){
                    g-=p+1;
                    pontos+=3;
                }
                else if (g==p){
                    pontos+=1;
                    g-=p;
                }
                else{
                    break;
                }                    
            }System.out.println(pontos);      
        }input.close();
    }
}