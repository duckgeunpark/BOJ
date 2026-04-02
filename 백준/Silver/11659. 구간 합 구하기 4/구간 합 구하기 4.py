# BOJ 11659 - 구간 합 구하기 4
# URL: https://www.acmicpc.net/problem/11659
# Tier: Silver III
# Tags: 누적 합

import sys

input = sys.stdin.readline


def solve() -> None:
    num, numsum = map(int, input().split())
    ranges = list(map(int, input().split()))
    prefix_sum = [0] * (num + 1)

    for i in range(num):
        prefix_sum[i + 1] = prefix_sum[i] + ranges[i]

    for _ in range(numsum):
        a, b = map(int, input().split())
        print(prefix_sum[b] - prefix_sum[a - 1])


if __name__ == "__main__":
    solve()
