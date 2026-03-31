# BOJ 8958 - OX퀴즈
# URL: https://www.acmicpc.net/problem/8958
# Tier: Bronze II
# Tags: 구현, 문자열

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    for i in range(n):
        sum = 0
        count = 0
        ox = list(input().strip())
        for oorx in ox:
            if oorx == "O":
                count += 1
                sum += count
            else:
                count = 0
        print(sum)


if __name__ == "__main__":
    solve()
