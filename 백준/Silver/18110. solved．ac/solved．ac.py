# BOJ 18110 - solved.ac
# URL: https://www.acmicpc.net/problem/18110
# Tier: Silver IV
# Tags: 수학, 구현, 정렬

import math
import sys

input = sys.stdin.readline


def normal_round(n):
    return math.floor(n + 0.5)


def solve() -> None:
    n = int(input())
    if n == 0:
        print(0)
        return

    score = []
    for i in range(n):
        score.append(int(input()))

    score.sort()
    cut = normal_round(n * 0.15)
    if cut == 0:
        trimmed = score  # 자르지 않고 전체 사용
    else:
        trimmed = score[cut:-cut]  # 앞뒤 cut개씩 제거

    avg = sum(trimmed) / len(trimmed)
    print(normal_round(avg))  # ✅ 평균도 일반 반올림 적용


if __name__ == "__main__":
    solve()

