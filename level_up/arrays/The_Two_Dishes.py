import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, S = map(int, input().split())
    ans = S if S < N else N - (S - N)
    print(ans)


