# BOJ 2903 - 중앙 이동 알고리즘
# URL: https://www.acmicpc.net/problem/2903
# Tier: Bronze III
# Tags: 수학

import sys
input = sys.stdin.readline

def solve() -> None:
    N = int(input())
    dot = 2
    for _ in range(N):
        dot = dot + (dot-1)
    print(dot**2)

if __name__ == "__main__":
    solve()
