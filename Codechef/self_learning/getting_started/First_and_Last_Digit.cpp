// https://www.codechef.com/LP0TO101/problems/FLOW004

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    while(T--) {
        string N;
        cin >> N;
        int ans = N[0] - '0' + N[N.length() - 1] - '0';
        cout << ans << "\n";
    }

    return 0;
}