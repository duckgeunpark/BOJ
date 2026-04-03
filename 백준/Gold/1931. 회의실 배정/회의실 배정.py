# BOJ 1931 - 회의실 배정
# URL: https://www.acmicpc.net/problem/1931
# Tier: Gold V
# Tags: 그리디 알고리즘, 정렬

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    circle = []
    for _ in range(n):
        a, b = map(int, input().split())
        circle.append([a, b])
    circle.sort(key=lambda x: (x[1], x[0]))

    count = 0
    end_time = 0

    for start, end in circle:
        if start >= end_time:
            count += 1
            end_time = end

    print(count)

if __name__ == "__main__":
    solve()

