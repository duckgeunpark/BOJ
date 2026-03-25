# BOJ 24723 - 녹색거탑
# URL: https://www.acmicpc.net/problem/24723
# Tier: Bronze IV
# Tags: 수학, 사칙연산

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    ans = 2**n
    print(ans)


if __name__ == "__main__":
    solve()
