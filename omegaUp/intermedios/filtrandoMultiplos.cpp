#include <iostream>
using namespace std;

int main()
{
    int cantidadDeNumetos, multiplo;
    cin >> cantidadDeNumetos;
    int arrayNumeros[cantidadDeNumetos];
    string cadenaResultante = "";

    for (int i = 0; i < cantidadDeNumetos; i++)
    {
        int numero;
        cin >> numero;
        arrayNumeros[i] = numero;
    }
    cin >> multiplo;

    for (int i = 0; i < cantidadDeNumetos; i++){
        if (arrayNumeros[i] % multiplo == 0){
            cout << arrayNumeros[i];
        }
        else{
            cout << "X";
        }
        cout<<" ";
    }
}