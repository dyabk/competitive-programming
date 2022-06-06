# CodeChef - Racing Horses - HORSES
# https://www.codechef.com/LP1TO201/problems/HORSES

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    
    S.sort()
    
    answer = min(S[i] - S[i - 1] for i in range(1, N))

    print(answer)