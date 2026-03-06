# BOJ 2292 - 벌집
# URL: https://www.acmicpc.net/problem/2292
# Tier: Bronze II
# Tags: 수학

import sys
input = sys.stdin.readline

def solve() -> None:
    N = int(input())
    room = 1
    while N > 1:
        N = N - (6 * room)
        room += 1
    print(room)

if __name__ == "__main__":
    solve()
