import java.util.Scanner;

public class ValorAbsoluto {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int suma = a + b;

        if (suma < 0)
            System.out.println(suma * -1);
        else
            System.out.println(suma);

        sc.close();
    }
}
