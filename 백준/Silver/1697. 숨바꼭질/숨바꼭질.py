# BOJ 1697 - 숨바꼭질
# URL: https://www.acmicpc.net/problem/1697
# Tier: Silver I
# Tags: 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque
import sys

input = sys.stdin.readline


def solve() -> None:
    start, end = map(int, input().split())
    max_pos = 100000
    time = [0] * (max_pos + 1)
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if now == end:
            print(time[now])
            break
        for next_step in (now - 1, now + 1, now * 2):
            if 0 <= next_step <= max_pos and time[next_step] == 0:
                time[next_step] = time[now] + 1
                queue.append(next_step)


if __name__ == "__main__":
    solve()
