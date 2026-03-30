# BOJ 2577 - 숫자의 개수
# URL: https://www.acmicpc.net/problem/2577
# Tier: Bronze II
# Tags: 수학, 구현, 사칙연산

import sys

input = sys.stdin.readline


def solve() -> None:
    a = int(input())
    b = int(input())
    c = int(input())
    mul = a * b * c
    mul_list = []
    while mul:
        mul_list.append(mul % 10)
        mul //= 10
    for i in range(10):
        print(mul_list.count(i))


if __name__ == "__main__":
    solve()
