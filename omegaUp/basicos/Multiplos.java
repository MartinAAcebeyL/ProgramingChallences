// url https://omegaup.com/arena/problem/multiplos_si_o_no/

import java.util.Scanner;

public class Multiplos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        if (a % b == 0 || b % a == 0)
            System.out.println("multiplos");
        else
            System.out.println("no multiplos");

        sc.close();
    }
}
