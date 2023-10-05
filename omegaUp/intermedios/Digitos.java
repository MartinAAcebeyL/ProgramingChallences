
// url: https://omegaup.com/arena/problem/digitos/
import java.util.Scanner;

public class Digitos {
    private static String crearSecuencia(int numero) {
        String r = "";
        for (int i = 1; i <= numero; i++) {
            r += i + "";
        }
        return r;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        char[] cadena = crearSecuencia(N).toCharArray();
        char[] N_array = Integer.toString(N).toCharArray();

        int index_N_array = 0;
        int index_inicio = 0;
        int longitud_N_array = N_array.length;
        for (int i = 0; i < cadena.length; i++) {
            if (index_N_array < longitud_N_array && cadena[i] == N_array[index_N_array]) {
                System.out.print(cadena[i] + "---" + N_array[index_N_array] + " ");
                index_N_array++;
                index_inicio = i + 1;
                System.out.println(index_inicio);
            } else {
                index_N_array = 0;
            }
            if (index_N_array >= longitud_N_array) {
                break;
            }
        }

        System.out.println(index_inicio - longitud_N_array + 1);

        sc.close();
    }
}
