
// url:  https://omegaup.com/arena/problem/gusano_escalador/
import java.util.Scanner;

public class GusanoEscalador {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int d, u, n;
        n = sc.nextInt();// longitud del poso
        u = sc.nextInt();// enrgia de subida
        d = sc.nextInt();// descenso

        boolean descanso = false;
        int cont = 0;
        while (n > 0) {
            if (!descanso)
                n -= u;
            else
                n += d;
            descanso = !descanso;
            cont++;
        }
        System.out.println(cont);
        sc.close();
    }
}
