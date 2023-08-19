// url: https://omegaup.com/arena/problem/Entrando-al-supermercado/
#include <iostream>
using namespace std;

int main(){
    int grupos, limite;
    cin >> grupos >> limite;
    int personas, cont = 0;

    for (int grupo = 0; grupo < grupos; grupo++){
        cin >> personas;
        if (cont+personas <= limite){
            cont+=personas;
            cout<<"pasa\n";
        }else{
            cout<<"espera\n";
        }
        
    }
}