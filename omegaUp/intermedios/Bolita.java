
// url: https://omegaup.com/arena/problem/bolita/
import java.util.Scanner;

public class Bolita {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Boolean arrayNueces[] = { false, false, false, false };
        int bolita = sc.nextInt();
        arrayNueces[bolita-1] = true;
        int movimientos = sc.nextInt();

        for (int i = 0; i < movimientos; i++) {
            int movimiento = sc.nextInt();
            switch (movimiento) {
                case 1:
                    Boolean temp = arrayNueces[0];
                    arrayNueces[0] = arrayNueces[1];
                    arrayNueces[1] = temp;
                    break;
                case 2:
                    temp = arrayNueces[0];
                    arrayNueces[0] = arrayNueces[2];
                    arrayNueces[2] = temp;
                    break;
                case 3:
                    temp = arrayNueces[0];
                    arrayNueces[0] = arrayNueces[3];
                    arrayNueces[3] = temp;
                    break;
                case 4:
                    temp = arrayNueces[1];
                    arrayNueces[1] = arrayNueces[2];
                    arrayNueces[2] = temp;
                    break;
                case 5:
                    temp = arrayNueces[1];
                    arrayNueces[1] = arrayNueces[3];
                    arrayNueces[3] = temp;
                    break;

                case 6:
                    temp = arrayNueces[2];
                    arrayNueces[2] = arrayNueces[3];
                    arrayNueces[3] = temp;
                    break;
            }
        }
        for (int i = 0; i < arrayNueces.length; i++) {
            if (arrayNueces[i] == true) {
                System.out.println(i + 1);
                break;
            }
        }
        sc.close();
    }

}
