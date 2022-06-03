// https://www.codechef.com/LP0TO101/problems/FLOW010

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    unordered_map<char, string> mp;
    mp['b'] = "BattleShip";
    mp['c'] = "Cruiser";
    mp['d'] = "Destroyer";
    mp['f'] = "Frigate";

    int T;
    cin >> T;
    while(T--){
        char id;
        cin >> id;
        id = tolower(id);
        cout << mp[id] << '\n';
    }

}