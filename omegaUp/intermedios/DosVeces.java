
// url: https://omegaup.com/arena/problem/Formateando-las-letras/

import java.util.Scanner;

class DosVeces {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextLine()) {
            String cadena = sc.nextLine();
            System.out.println(cadena.toUpperCase());
            System.out.println(cadena.toLowerCase());
        }
        sc.close();
    }
}