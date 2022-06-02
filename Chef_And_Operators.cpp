// https://www.codechef.com/LP0TO101/problems/CHOPRT

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    while(T--) {
        int A, B;
        cin >> A >> B;

        if (A < B) {
            cout << "<" << "\n";
        }
        else if (A > B) {
            cout << ">" << "\n";
        }
        else {
            cout << "=" << "\n";
        }
    }

    return 0;
}