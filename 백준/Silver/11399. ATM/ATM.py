# BOJ 11399 - ATM
# URL: https://www.acmicpc.net/problem/11399
# Tier: Silver IV
# Tags: 그리디 알고리즘, 정렬

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    total = 0
    current = 0
    for t in nums:
        current += t  # 내 앞사람들 + 내 인출 시간
        total += current  # 전체 합에 추가
    print(total)


if __name__ == "__main__":
    solve()
