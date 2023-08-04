import java.util.Scanner;

public class MCDRecursivo {
    private static float mcd(float num1, float num2) {
        float max = num1 >= num2 ? num1 : num2;
        float min = num1 <= num2 ? num1 : num2;

        if (max % min == 0) {
            return min;
        } else {
            return mcd(min, max % min);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Float num1 = sc.nextFloat();
        Float num2 = sc.nextFloat();
        System.out.println(mcd(num1, num2));

        sc.close();
    }
}
