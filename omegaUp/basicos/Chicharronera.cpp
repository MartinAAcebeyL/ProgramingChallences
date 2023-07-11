// url:

#include <iostream>
#include <math.h>
using namespace std;

int formula(double, double, double, bool positivo);

int main()
{
    double A, B, C;
    cin >> A >> B >> C;
    cout << formula(A, B, C, true) << " " << formula(A, B, C, false);
    return 0;
}

int formula(double A, double B, double C, bool positivo)
{
    if (positivo)
        return (-B + sqrt(pow(B, 2) - 4 * A * C)) / 2 * A;
    return (-B - sqrt(pow(B, 2) - 4 * A * C)) / 2 * A;
}