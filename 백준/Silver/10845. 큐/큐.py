# BOJ 10845 - 큐
# URL: https://www.acmicpc.net/problem/10845
# Tier: Silver IV
# Tags: 자료 구조, 큐

import sys
from collections import deque

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    q = deque()
    for i in range(n):
        cmd = input().split()
        if cmd[0] == "push":
            q.append(cmd[1])
        elif cmd[0] == "pop":
            print(q.popleft() if q else -1)
        elif cmd[0] == "size":
            print(len(q))
        elif cmd[0] == "empty":
            print(0 if q else 1)
        elif cmd[0] == "front":
            print(q[0] if q else -1)
        elif cmd[0] == "back":
            print(q[-1] if q else -1)


if __name__ == "__main__":
    solve()
