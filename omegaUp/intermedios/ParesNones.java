import java.util.Scanner;

class ParesNones {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sumaPares = 0;
        int contadorPares = 0;
        int sumaImpares = 0;

        for (int i = 0; i < n; i++) {
            int carta = sc.nextInt();
            if(carta%2==0){
                sumaPares+=carta;
                contadorPares+=1;
            }else{
                sumaImpares+=carta;
            }
        }

        if(sumaPares/contadorPares>sumaImpares/(n-contadorPares)){
            System.out.println("APARICIO");
        }else if(sumaPares/contadorPares<sumaImpares/(n-contadorPares)){
            System.out.println("NONILA");
        }else{
            System.out.println("EMPATE!");
        }

        sc.close();
    }

}