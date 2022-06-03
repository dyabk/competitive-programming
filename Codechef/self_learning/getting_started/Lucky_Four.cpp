// https://www.codechef.com/LP0TO101/problems/LUCKFOUR

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    while(T--) {
        string num;
        cin >> num;

        int ans = count(num.begin(), num.end(), '4');
        cout << ans << "\n";
    }

    return 0;
}