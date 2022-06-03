# CodeChef - MXEVNSUB - Maximum Length Even Subarray
# https://www.codechef.com/LP1TO201/problems/MXEVNSUB

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    first, last, length = 1, N, N
    while True:
        _sum = (first + last) * (length) // 2
        if _sum % 2 == 0:
            break
        else:
            first += 1
            length -= 1
        
    print(length)