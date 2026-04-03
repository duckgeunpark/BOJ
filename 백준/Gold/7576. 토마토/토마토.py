# BOJ 7576 - 토마토
# URL: https://www.acmicpc.net/problem/7576
# Tier: Gold V
# Tags: 너비 우선 탐색, 그래프 이론, 그래프 탐색, 격자 그래프, 최단 경로

from collections import deque
import sys

input = sys.stdin.readline


def solve() -> None:
    # M=가로, N=세로
    M, N = map(int, input().split())
    tomato = []
    queue = deque()
    for i in range(N):
        tomato.append(list(map(int, input().split())))
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append([i, j])
    # 상하좌우 이동방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append([nx, ny])

    days = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                print(-1)
                return
            days = max(days, tomato[i][j])

    print(days - 1)


if __name__ == "__main__":
    solve()
