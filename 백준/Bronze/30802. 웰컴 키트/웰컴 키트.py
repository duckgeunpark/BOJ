# BOJ 30802 - 웰컴 키트
# URL: https://www.acmicpc.net/problem/30802
# Tier: Bronze III
# Tags: 수학, 구현, 사칙연산

import math
import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    Tshirt = list(map(int, input().split()))
    pen = list(map(int, input().split()))
    count = 0
    for i in Tshirt:
        count += math.ceil(i / pen[0])
    print(count)
    ans_pen = []
    ans_pen.append(n // pen[1])
    ans_pen.append(n % pen[1])
    print(*ans_pen)


if __name__ == "__main__":
    solve()
