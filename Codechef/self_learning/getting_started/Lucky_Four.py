# https://www.codechef.com/LP0TO101/problems/LUCKFOUR

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    num = input().rstrip()
    ans = num.count('4')
    print(ans)