import java.util.Scanner;

class Triangulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float a, b;
        a = sc.nextFloat();
        b = sc.nextFloat();

        System.out.println((a * b) / 2);
        sc.close();
    }
}