# BOJ 11724 - 연결 요소의 개수
# URL: https://www.acmicpc.net/problem/11724
# Tier: Silver II
# Tags: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque
import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            count += 1

            queue = deque([i])
            visited[i] = True

            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    print(count)


if __name__ == "__main__":
    solve()
