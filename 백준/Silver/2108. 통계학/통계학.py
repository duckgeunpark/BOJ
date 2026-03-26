# BOJ 2108 - 통계학
# URL: https://www.acmicpc.net/problem/2108
# Tier: Silver II
# Tags: 수학, 구현, 정렬

import sys

input = sys.stdin.readline
from collections import Counter


def solve() -> None:
    n = int(input())
    nums = []
    for _ in range(n):
        numb = int(input())
        nums.append(numb)
    nums.sort()
    print(round(sum(nums) / n))  # ✓ 반올림
    print(nums[n // 2])

    counter = Counter(nums)
    max_freq = max(counter.values())  # 최대 빈도수

    # 최빈값만 추출 후 정렬
    modes = sorted([k for k, v in counter.items() if v == max_freq])

    # 최빈값 여러 개면 두 번째, 하나면 그냥 출력
    if len(modes) > 1:
        print(modes[1])  # 두 번째로 작은 값
    else:
        print(modes[0])

    print(max(nums) - min(nums))


if __name__ == "__main__":
    solve()
