// url: https://omegaup.com/arena/problem/Contando-Letras/

import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

class ContandoLetras {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String abc = "abcdefghijklmnopqrstuvwxyz";
        Map<Character, Integer> contador = new HashMap<>();

        for (int i = 0; i < abc.length(); i++) {
            contador.put(abc.charAt(i), 0);
        }
        int I = sc.nextInt();
        int F = sc.nextInt();


        String cadena = sc.next();
        for (int i = I; i < F; i++) {
            char letra = cadena.charAt(i);
            if (letra != ' ') {
                int count = contador.get(letra);
                contador.put(letra, count + 1);
            }
        }

        for (char letra : contador.keySet()) {
            int count = contador.get(letra);
            System.out.println(letra + "=" + count);
        }

        sc.close();
    }
}