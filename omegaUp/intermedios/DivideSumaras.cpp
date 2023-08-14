#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int cont = 0;
    for (int i = 0; i < N; i++)
    {
        cont += N / pow(2, i);
    }
    cout << cont;
    return 0;
}