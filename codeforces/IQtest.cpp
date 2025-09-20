#include<iostream>

using namespace std;


int main(){
    int amount;
    cin >> amount;

    int last_even_index=0;
    int last_odd_index = 0;

    int even_amount = 0;
    int odd_amount = 0;

    for (int i = 0; i < amount; i++){
        int n;
        cin >> n;
        if(n%2==0){
            last_even_index=i;
            even_amount+=1;
        }else{
            last_odd_index = i;
            odd_amount += 1;
        }
    }
    int response = even_amount < odd_amount ? last_even_index : last_odd_index;

    cout << response+1;
    return 0;
}