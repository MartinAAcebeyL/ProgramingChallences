#include <iostream>
#include<cmath>

using namespace std;

int main(){
    int A, B, C;
    cin >> A >> B >> C;
    if(abs(C-A)<abs(C-B)){
        cout<<"gato A";
    }else if(abs(C-B)<abs(C-A)){
        cout << "gato B";
    }else{
        cout << "raton C";
    }
    return 0;
}