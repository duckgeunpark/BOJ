# BOJ 11049 - 행렬 곱셈 순서
# URL: https://www.acmicpc.net/problem/11049
# Tier: Gold III
# Tags: 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

def solve() -> None:
    n = int(input())
    matrices = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            
                if cost < dp[i][j]:
                    dp[i][j] = cost
            
    print(dp[0][n-1])
        

if __name__ == "__main__":
    solve()
