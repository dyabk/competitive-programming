# CodeChef - TWOSTR - Chef and the Wildcard Matching
# https://www.codechef.com/LP1TO201/problems/TWOSTR

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X = input().rstrip()
    Y = input().rstrip()

    ans = "Yes"
    for i in range(len(X)):
        if X[i] != Y[i] and X[i] != '?' and Y[i] != '?':
            ans = "No"
            break

    print(ans)