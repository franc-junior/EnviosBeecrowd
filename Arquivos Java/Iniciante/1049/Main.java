package pkg1049;

import java.util.Scanner;
public class Main {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String animal = "";
        
        String a = input.nextLine();
        String b = input.nextLine();
        String c = input.nextLine();
        if(a.equals("vertebrado")){
            if(b.equals("ave")){
                if(c.equals("carnivoro")){
                    animal = "aguia";
                }else{
                    animal = "pomba";
                } 
            }else{
                if(c.equals("onivoro")){
                    animal = "homem";
                }else{
                    animal = "vaca";
                }
            }  
        }else{
            if(b.equals("inseto")){
                if(c.equals("hematofago")){
                    animal = "pulga";
                }else{
                    animal = "lagarta";
                } 
            }else{
                if(c.equals("hematofago")){
                    animal = "sanguessuga";
                }else{
                    animal = "minhoca";
                }
            }
        }
        System.out.println(animal);   
    } 
}
