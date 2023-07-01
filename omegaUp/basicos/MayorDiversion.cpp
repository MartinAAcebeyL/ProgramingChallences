#include <iostream>
using namespace std;

int main()
{
    int cantidadJuguetes;
    cin >> cantidadJuguetes;
    int sumatoria = 0;
    int jugueteDeMenorDiversion = 10000;

    for (int i = 0; i < cantidadJuguetes; i++)
    {
        int juguete;
        cin >> juguete;
        sumatoria += juguete;
        if (juguete < jugueteDeMenorDiversion)
            jugueteDeMenorDiversion = juguete;
    }
    cout << sumatoria-jugueteDeMenorDiversion;
    return 0;
}