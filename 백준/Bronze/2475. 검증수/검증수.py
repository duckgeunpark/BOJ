# BOJ 2475 - 검증수
# URL: https://www.acmicpc.net/problem/2475
# Tier: Bronze V
# Tags: 구현, 사칙연산, 수학

import sys

input = sys.stdin.readline


def solve() -> None:
    nums = list(map(int, input().split()))
    print(sum(x ** 2 for x in nums) % 10)



if __name__ == "__main__":
    solve()
