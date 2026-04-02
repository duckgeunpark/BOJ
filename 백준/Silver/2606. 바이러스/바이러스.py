# BOJ 2606 - 바이러스
# URL: https://www.acmicpc.net/problem/2606
# Tier: Silver III
# Tags: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque
import sys

input = sys.stdin.readline


def solve() -> None:
    cpt = int(input())
    edges = int(input())

    graph = [[] for _ in range(cpt + 1)]
    for i in range(edges):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (cpt + 1)
    visited[1] = True
    queue = deque([1])
    count = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    print(count)


if __name__ == "__main__":
    solve()
