#include <iostream>
using namespace std;

bool esSemiCuadradoMagico(int _array[][100], int size)
{
    int sumaPrincipal = 0;
    int sumaSecundaria = 0;

    for (int i = 0; i < size; i++)
    {
        sumaPrincipal += _array[i][i];
        sumaSecundaria += _array[i][size - 1 - i];
    }

    for (int i = 0; i < size; i++)
    {
        int sumaFila = 0;
        int sumaColumna = 0;
        for (int j = 0; j < size; j++)
        {
            sumaFila += _array[i][j];
            sumaColumna += _array[j][i];
        }
        if (sumaFila != sumaPrincipal || sumaColumna != sumaPrincipal)
            return false;
    }

    return sumaPrincipal == sumaSecundaria;
}

int main()
{
    int size;
    cin >> size;
    int _array[size][100];
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            int n;
            cin >> n;
            _array[i][j] = n;
        }
    }

    if (esSemiCuadradoMagico(_array, size))
        cout << 1;
    else
        cout << 0;

    return 0;
}
