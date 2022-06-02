// https://www.codechef.com/LP0TO101/problems/FLOW007

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    while (T--) {
        string N;
        cin >> N;
        reverse(N.begin(), N.end());
        int ans = stoi(N);
        cout << ans << "\n";
    }

    return 0;
}