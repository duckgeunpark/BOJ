# BOJ 2805 - 나무 자르기
# URL: https://www.acmicpc.net/problem/2805
# Tier: Silver II
# Tags: 이분 탐색, 매개 변수 탐색

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())
    tree_h = list(map(int, input().split()))
    start = 0
    end = max(tree_h)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total_cut = sum(tree - mid for tree in tree_h if tree > mid)

        if total_cut < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)


if __name__ == "__main__":
    solve()
