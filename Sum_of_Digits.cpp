// https://www.codechef.com/LP0TO101/problems/INTEST

#include <bits/stdc++.h>
using namespace std;

int main() {
    
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    while(T--){
        string N;
        cin >> N;
        int ans = 0;
        for(char & d : N){
            ans += d - '0';
        }
        cout << ans << '\n';
    }

}