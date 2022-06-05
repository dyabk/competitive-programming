# CodeChef - ERROR - Chef and Feedback
# https://www.codechef.com/LP1TO201/problems/ERROR

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = input().rstrip()

    ans = "Bad"
    if S.find("010") != -1 or S.find("101") != -1:
        ans = "Good"
    
    print(ans)