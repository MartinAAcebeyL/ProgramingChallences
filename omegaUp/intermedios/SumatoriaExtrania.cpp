#include <iostream>
using namespace std;

int sumatoria(int, int);

int main(){
    int a, b;
    cin >> a >> b;

    int m = sumatoria(a, 1);
    int n = sumatoria(b, 1);

    cout << sumatoria(n, m);
    return 0;
}

int sumatoria(int n, int inicio){
    int _sumatoria = 0;
    for (int i = inicio; i <= n; i++){
        _sumatoria += i;
    }
    return _sumatoria;
}