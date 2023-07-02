
// url: https://omegaup.com/arena/problem/Calculadora-de-salario-UAMA-PE/
import java.util.Scanner;

class CalculoSalario {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int horasTrabajo = sc.nextInt();
        double sueldo = sc.nextDouble();

        double salario = calcularSalarioTotal(horasTrabajo, sueldo);

        System.out.println(salario);
        sc.close();
    }

    public static double calcularSalarioTotal(int horasTrabajo, double sueldoPorHora) {
        int horasRegulares = Math.min(horasTrabajo, 40);
        int horasExtras1 = Math.min(Math.max(horasTrabajo - 40, 0), 10);
        int horasExtras2 = Math.max(horasTrabajo - 50, 0);
        double salario = horasRegulares * sueldoPorHora
                + horasExtras1 * sueldoPorHora * 1.5
                + horasExtras2 * sueldoPorHora * 2;

        return salario;
    }
}