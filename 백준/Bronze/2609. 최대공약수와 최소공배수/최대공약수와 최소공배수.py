# BOJ 2609 - 최대공약수와 최소공배수
# URL: https://www.acmicpc.net/problem/2609
# Tier: Bronze I
# Tags: 수학, 정수론, 유클리드 호제법

import sys

input = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


def solve() -> None:
    a, b = map(int, input().split())
    sol = gcd(a, b)
    ans = (a * b) // gcd(a, b)
    print(sol)
    print(ans)


if __name__ == "__main__":
    solve()
