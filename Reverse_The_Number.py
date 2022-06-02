# https://www.codechef.com/LP0TO101/problems/FLOW007

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    print(((input()[::-1]).lstrip('0')).strip())