# BOJ 10872 - 팩토리얼
# URL: https://www.acmicpc.net/problem/10872
# Tier: Bronze III
# Tags: 수학, 구현

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    ans = 1
    while n:
        ans *= n
        n -= 1
    print(ans)


if __name__ == "__main__":
    solve()
