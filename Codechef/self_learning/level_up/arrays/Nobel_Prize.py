# CodeChef - NOBEL - Nobel Prize
# https://www.codechef.com/LP1TO201/problems/NOBEL

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
   N, M = map(int, input().split())
   taken_topics = set()
   A = list(map(int, input().split()))
   for i in range(N):
       taken_topics.add(A[i])
   ans = "Yes" if len(taken_topics) < M else "No"
   print(ans)