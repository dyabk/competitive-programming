#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio("0");
    cin.tie(0);

    const double WITHDRAWAL_CHARGE = 0.50;

    int X;
    cin >> X;
    double Y;
    cin >> Y;

    if (X % 5 == 0 && Y >= X + WITHDRAWAL_CHARGE) {
        Y -= X + WITHDRAWAL_CHARGE;
    }

    printf("%.2lf", Y);

    return 0;
}