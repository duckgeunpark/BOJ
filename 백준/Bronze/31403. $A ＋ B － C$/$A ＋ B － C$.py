# BOJ 31403 - $A + B - C$
# URL: https://www.acmicpc.net/problem/31403
# Tier: Bronze IV
# Tags: 수학, 문자열, 사칙연산

import sys

input = sys.stdin.readline


def solve() -> None:
    a = input().strip()
    b = input().strip()
    c = input().strip()

    print((int(a) + int(b)) - int(c))
    print(int(a + b) - int(c))


if __name__ == "__main__":
    solve()
