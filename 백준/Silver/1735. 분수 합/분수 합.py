# BOJ 1735 - 분수 합
# URL: https://www.acmicpc.net/problem/1735
# Tier: Silver III
# Tags: 수학, 정수론, 유클리드 호제법

import sys

input = sys.stdin.readline


def gcd(a: int, b: int) -> int:

    while b > 0:
        a, b = b, a % b
    return a


def solve() -> None:
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    mother = b * d
    son = (a * d) + (c * b)

    ans = gcd(son, mother)

    mother //= ans
    son //= ans

    print(son, mother)


if __name__ == "__main__":
    solve()
