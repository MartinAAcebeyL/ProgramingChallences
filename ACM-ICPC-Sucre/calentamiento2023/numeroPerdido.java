import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static int encontrarCartaFaltante(int cantidad, int[] cartas) {
        int sumaTotal = (cantidad * (cantidad + 1)) / 2;
        int sumaActual = Arrays.stream(cartas).sum();

        int cartaFaltante = sumaTotal - sumaActual;
        return cartaFaltante;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int cantidad = scanner.nextInt();
        int[] cartas = new int[cantidad];

        for (int i = 0; i < cantidad; i++) {
            cartas[i] = scanner.nextInt();
        }

        int cartaFaltante = encontrarCartaFaltante(cantidad, cartas);
        System.out.println(cartaFaltante);
    }
}