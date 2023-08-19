#include <iostream>
#include <string>
#include <limits>

using namespace std;

int main(){
    int cantidad_palabras;
    int longitud_palabra = numeric_limits<int>::max();
    cin >> cantidad_palabras;
    string palabra;
    
    for (int i = 0; i < cantidad_palabras; i++){
        string p;
        cin>>p;
        int longitud=p.length();
        if(longitud<longitud_palabra){
            longitud_palabra=longitud;
            palabra=p;
        }
    }
    string par_impar=(palabra.length()%2==0)?"par":"impar";
    cout << palabra << "\n";
    cout << palabra.length() << "\n";
    cout << par_impar << "\n";

    return 0;
}
