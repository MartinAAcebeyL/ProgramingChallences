#include <iostream>

using namespace std;

int main()
{
    int cantidadNumeros;
    cin >> cantidadNumeros;
    int arregloNumeros[cantidadNumeros];
    for (int i = 0; i < cantidadNumeros; i++){
        int numero;
        cin >> numero;
        arregloNumeros[i] = numero;
    }

    for (int i = 0; i < cantidadNumeros / 2; i++){
        int suma = arregloNumeros[i] + arregloNumeros[cantidadNumeros - i-1];
        cout << suma << " ";
    }
    
    return 0;
}