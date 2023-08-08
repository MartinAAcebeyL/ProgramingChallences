
// url: https://omegaup.com/arena/problem/Rifa/
import java.util.Scanner;

public class Rifa {

    private static int sumatoria(int numero) {
        int suma = 0;
        for (int i = 1; i <= numero; i++) {
            suma += 1;
        }
        return suma;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int dinero = 0;
        for (int i = 0; i < N; i++) {
            int M = sc.nextInt();
            dinero += sumatoria(M);
        }
        System.out.println(dinero);
        sc.close();
    }
}
