# BOJ 13241 - 최소공배수
# URL: https://www.acmicpc.net/problem/13241
# Tier: Silver V
# Tags: 수학, 정수론, 유클리드 호제법

import sys

input = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b

    return a


def solve() -> None:
    a, b = map(int, input().split())
    sol = (a * b) // gcd(a, b)
    print(sol)


if __name__ == "__main__":
    solve()

