
// url:https://omegaup.com/arena/problem/Simulando-un-Display/
import java.util.Scanner;

class Display {

    private static String[] crearNumero(char caracter) {
        String uno[] = { "# ", "# ", "# ", "# ", "# " };
        String dos[] = { "### ", "  # ", "### ", "#   ", "### " };
        String tres[] = { "### ", "  # ", "### ", "  # ", "### " };
        String cuatro[] = { "# # ", "# # ", "### ", "  # ", "  # " };
        String cinco[] = { "### ", "#   ", "### ", "  # ", "### " };
        String seis[] = { "### ", "#   ", "### ", "# # ", "### " };
        String siete[] = { "### ", "  # ", "  # ", "  # ", "  # " };
        String ocho[] = { "### ", "# # ", "### ", "# # ", "### " };
        String nueve[] = { "### ", "# # ", "### ", "  # ", "### " };
        String cero[] = { "### ", "# # ", "# # ", "# # ", "### " };
        String numeros[][] = { cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve };
        String numero[] = numeros[Character.getNumericValue(caracter)];
        return numero;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String numeros = sc.next();
        char caracter = sc.next().charAt(0);

        String array_numeros[][] = new String[numeros.length()][5];

        for (int i = 0; i < numeros.length(); i++) {
            array_numeros[i] = crearNumero(numeros.charAt(i));
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < numeros.length(); j++) {
                String linea = array_numeros[j][i].replace("#", caracter + "");
                System.out.print(linea);
            }
            System.out.println();
        }

        sc.close();
    }
}
