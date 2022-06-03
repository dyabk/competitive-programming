// https://www.codechef.com/LP1TO201/problems/CHFRICH

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    while(T--) {
        int A, B, X;
        cin >> A >> B >> X;
        int ans = (B - A) / X;
        cout << ans << "\n";
    }

    return 0;
}