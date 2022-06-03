# CodeChef - PROBCAT - Problem Category
# https://www.codechef.com/LP1TO201/problems/PROBCAT

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x = int(input())
    ans = "Easy"
    if 100 <= x < 200:
        ans = "Medium"
    elif 200 <= x <= 300:
        ans = "Hard"
    print(ans)