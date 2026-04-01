# BOJ 2775 - 부녀회장이 될테야
# URL: https://www.acmicpc.net/problem/2775
# Tier: Bronze I
# Tags: 수학, 구현, 다이나믹 프로그래밍

import sys

input = sys.stdin.readline


def solve() -> None:
    t = int(input())
    for _ in range(t):
        k = int(input())  # 층 (k)
        n = int(input())  # 호 (n)

        # 0층의 사람 수 리스트 초기화 [1, 2, 3, ..., n]
        floor = [i for i in range(1, n + 1)]

        # k층만큼 반복하면서 사람 수 누적
        for _ in range(k):
            for j in range(1, n):  # 2호실(인덱스 1)부터 끝까지
                # 내 호실 사람 수 = (같은 층 이전 호실) + (아래층 내 호실)
                floor[j] += floor[j - 1]

        print(floor[-1])  # 마지막 호실의 사람 수 출력


if __name__ == "__main__":
    solve()
