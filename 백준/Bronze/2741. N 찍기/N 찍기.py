# BOJ 2741 - N 찍기
# URL: https://www.acmicpc.net/problem/2741
# Tier: Bronze V
# Tags: 구현

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    for i in range(1, n + 1):
        print(i)


if __name__ == "__main__":
    solve()
