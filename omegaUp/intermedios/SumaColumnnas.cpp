// url:
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n][n];

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            int numero;
            cin >> numero;
            array[i][j] = numero;
        }
    }

    for (int i = 0; i < n; i++){
        int sum = 0;
        for (int j = 0; j < n; j++){
            sum+=array[j][i];
        }
        cout<<sum<<" ";
    }

    return 0;
}