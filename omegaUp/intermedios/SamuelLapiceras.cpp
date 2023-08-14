#include <iostream>
using namespace std;

int main()
{
    int lapiceras;
    cin >> lapiceras;

    float suma = 0;
    for (int i = 0; i < lapiceras; i++)
    {
        int n;
        cin >> n;
        suma += n;
    }

    float result = suma / lapiceras;
    cout << result;

    return 0;
}