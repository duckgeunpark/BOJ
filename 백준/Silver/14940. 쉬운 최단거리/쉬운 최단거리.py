# BOJ 14940 - 쉬운 최단거리
# URL: https://www.acmicpc.net/problem/14940
# Tier: Silver I
# Tags: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 격자 그래프

from collections import deque
import sys

input = sys.stdin.readline


def solve() -> None:
    # n세로,  m가로
    n, m = map(int, input().split())
    graph = []
    # 1. 정답을 담을 배열: 도달할 수 없는 곳은 -1로 출력하라는 조건 때문에 -1로 초기화
    ans = [[-1] * m for _ in range(n)]

    start_x, start_y = 0, 0

    # 2. 지도 입력과 동시에 목표 지점(2)과 벽(0) 찾기
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(m):
            if row[j] == 2:
                start_x, start_y = i, j
                ans[i][j] = 0  # 목표 지점 자신의 거리는 0
            elif row[j] == 0:
                ans[i][j] = 0  # 원래 갈 수 없는 땅도 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 지도를 벗어나지 않고
            if 0 <= nx < n and 0 <= ny < m:
                # 갈 수 있는 땅(1)이면서 아직 방문하지 않은 곳(-1)이라면
                if graph[nx][ny] == 1 and ans[nx][ny] == -1:
                    # 현재까지 온 거리 + 1을 정답 배열에 바로 기록
                    ans[nx][ny] = ans[x][y] + 1
                    queue.append((nx, ny))
    for i in range(n):
        print(*ans[i])


if __name__ == "__main__":
    solve()
