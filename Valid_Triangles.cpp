// https://www.codechef.com/LP0TO101/problems/FLOW013

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    while(T--) {
        int A, B, C;
        cin >> A >> B >> C;
        string ans = A + B + C == 180 ? "YES" : "NO";
        cout << ans << "\n";
    }
    
    return 0;
}