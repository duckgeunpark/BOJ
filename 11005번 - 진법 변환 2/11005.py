# BOJ 11005 - 진법 변환 2
# URL: https://www.acmicpc.net/problem/11005
# Tier: Bronze I
# Tags: 수학, 구현

import sys
input = sys.stdin.readline

def solve(N, B) -> None:
    N, B = input().split()
    B = int(B)

    return hex(int(N, B))[2:].upper()

if __name__ == "__main__":
    solve()
