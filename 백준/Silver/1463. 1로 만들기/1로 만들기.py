# BOJ 1463 - 1로 만들기
# URL: https://www.acmicpc.net/problem/1463
# Tier: Silver III
# Tags: 다이나믹 프로그래밍

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    print(dp[n])


if __name__ == "__main__":
    solve()
