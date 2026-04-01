# BOJ 14626 - ISBN
# URL: https://www.acmicpc.net/problem/14626
# Tier: Bronze I
# Tags: 수학, 구현, 브루트포스 알고리즘, 사칙연산

import sys

input = sys.stdin.readline


def solve() -> None:
    isbn = list(input().strip())
    sol = 0
    x = 1
    for i in range(13):
        if isbn[i] == "*":
            x = 3 if i % 2 != 0 else 1
        else:
            val = int(isbn[i])
            sol += val * 3 if i % 2 != 0 else val
    for d in range(10):
        if (sol + d * x) % 10 == 0:
            print(d)
            break


if __name__ == "__main__":
    solve()
