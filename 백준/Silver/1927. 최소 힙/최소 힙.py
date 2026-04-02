# BOJ 1927 - 최소 힙
# URL: https://www.acmicpc.net/problem/1927
# Tier: Silver II
# Tags: 자료 구조, 우선순위 큐


import sys
import heapq

input = sys.stdin.readline


def solve() -> None:
    heap = []
    n = int(input())
    for _ in range(n):
        num = int(input())

        if num == 0:
            if len(heap) > 0:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, num)


if __name__ == "__main__":
    solve()
