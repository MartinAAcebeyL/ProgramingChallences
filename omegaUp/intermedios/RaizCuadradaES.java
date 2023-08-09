
// url: https://omegaup.com/arena/problem/Raiz-cuadrada-entrada-y-salida/
import java.util.Scanner;

public class RaizCuadradaES {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int D = sc.nextInt();
        String formato = "%." + D + "f";
        String numeroFormateado = String.format(formato, Math.sqrt(N));
        System.out.println(numeroFormateado);
        sc.close();
    }
}
