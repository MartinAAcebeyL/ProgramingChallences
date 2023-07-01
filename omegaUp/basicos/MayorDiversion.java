import java.util.Scanner;

public class MayorDiversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int sum = 0;
        int menor = 101;
        
        for (int i = 0; i < number; i++) {
            int diversion = scanner.nextInt();
            sum += diversion;
            if (diversion < menor)
                menor = diversion;
        }
        
        scanner.close();
        System.out.println(sum-menor);
    }
}