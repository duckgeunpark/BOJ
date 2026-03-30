# BOJ 2920 - 음계
# URL: https://www.acmicpc.net/problem/2920
# Tier: Bronze II
# Tags: 구현

import sys

input = sys.stdin.readline


def solve() -> None:
    n = list(map(int, input().split()))
    if n == list(range(1, 9)):
        print("ascending")
    elif n == list(range(8, 0, -1)):
        print("descending")
    else:
        print("mixed")


if __name__ == "__main__":
    solve()
