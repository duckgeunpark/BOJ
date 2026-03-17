# BOJ 2485 - 가로수
# URL: https://www.acmicpc.net/problem/2485
# Tier: Silver IV
# Tags: 수학, 정수론, 유클리드 호제법

import sys
import math

input = sys.stdin.readline


def solve() -> None:
    n = int(input())

    trees = [int(input()) for _ in range(n)]

    gaps = []
    for i in range(n - 1):
        gaps.append(trees[i + 1] - trees[i])

    current_gcd = gaps[0]
    for i in range(1, len(gaps)):
        current_gcd = math.gcd(current_gcd, gaps[i])

    total_trees = (trees[-1] - trees[0]) // current_gcd + 1
    added_trees = total_trees - n

    print(added_trees)


if __name__ == "__main__":
    solve()
