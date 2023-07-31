import java.util.Scanner;

class PorfirioDonas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        int[] NArray = new int[N];

        for (int i = 0; i < N; i++) {
            int numero = sc.nextInt();
            NArray[i] = numero;
        }

        for (int i = 0; i < N; i++) {
            System.out.println(seRealizaraFiesta(A, B, NArray[i]));
        }

        sc.close();
    }

    public static String seRealizaraFiesta(int A, int B, int numero) {
        if (numero < A && numero < B)
            return "No";
        while (numero >= A || numero >= B) {
            if (numero >= B && numero > A)
                numero -= B;
            if (numero >= A)
                numero -= A;
        }
        return numero <= 0 ? "Si" : "No";
    }
}