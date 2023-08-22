#include <iostream>

using namespace std;

int main()
{
    int cantidadCasos;
    cin >> cantidadCasos;
    for (int i = 0; i < cantidadCasos; i++)
    {
        int numeroMurrallas;
        cin >> numeroMurrallas;
        int aux = 0;
        int brincosAltos = 0, brincosBajos = 0;

        for (int i = 0; i < numeroMurrallas; i++)
        {
            int murralla;
            cin >> murralla;
            if (i == 0)
            {
                aux = murralla;
                continue;
            }
            if (murralla > aux)
            {
                brincosAltos++;
            }
            else if (murralla < aux)
            {
                brincosBajos++;
            }
            aux = murralla;
        }
        cout << "Escenario " << i + 1 << ": " << brincosAltos << " " << brincosBajos << "\n";
    }

    return 0;
}