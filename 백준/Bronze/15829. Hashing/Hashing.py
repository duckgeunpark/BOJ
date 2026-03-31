# BOJ 15829 - Hashing
# URL: https://www.acmicpc.net/problem/15829
# Tier: Bronze II
# Tags: 구현, 문자열, 해싱

import sys

input = sys.stdin.readline
MOD = 1234567891


def solve() -> None:
    n = int(input())
    alpa = list(input().strip())
    alpatonum = []
    ans = 0
    for i in range(n):
        ans += (ord(alpa[i]) - 96) * (31**i)
    print(ans % MOD)


if __name__ == "__main__":
    solve()
